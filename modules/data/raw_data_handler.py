############## Import Files ##################
import os
import json                             # to read in fraud JSON
import pandas as pd                     # data frames

############## Class Definition ##################
class RawDataHandler:
    """
    Handles extraction, transformation, and description of raw data for machine learning preprocessing.
    """

    ############## Initialization ##################
    def __init__(self, storage_path, save_path):
        self.storage_path = storage_path            # where data lives
        self.save_path = save_path                  # where to save outputs, if we need to later

    ############## Extract Raw ##################
    def extract(self, customer_information_filename, transaction_filename, fraud_information_filename):
        # full file paths
        customer_path = os.path.join(self.storage_path, customer_information_filename)
        transaction_path = os.path.join(self.storage_path, transaction_filename)
        fraud_path = os.path.join(self.storage_path, fraud_information_filename)

        # Load data
        customer_df = pd.read_csv(customer_path)              # customer info CSV
        transaction_df = pd.read_parquet(transaction_path)    # transactions parquet
        with open(fraud_path, 'r') as f:
            fraud_data = json.load(f)                         # fraud JSON

        fraud_df = pd.DataFrame({'is_fraud': fraud_data})     # convert fraud list to DataFrame

        return customer_df, transaction_df, fraud_df          # return all 3

    ############## Convert Date-Time ##################
    def convert_dates(self, df):
        df = df.copy()                                        # don't modify original
        dt = pd.to_datetime(df['trans_date_trans_time'])     # parse datetime

        # Extract time features, love me some pandas
        df['day_of_week'] = dt.dt.day_name()
        df['hour'] = dt.dt.hour
        df['minute'] = dt.dt.minute
        df['seconds'] = dt.dt.second
        df['day_date'] = dt.dt.day
        df['month_date'] = dt.dt.month_name()
        df['year_date'] = dt.dt.year

        df.drop(columns=['trans_date_trans_time'], inplace=True)  # drop original datetime column

        return df

    ############## merge/clean ##################
    def transform(self, customer_df, transaction_df, fraud_df):
        transaction_df = transaction_df.copy()
        transaction_df['is_fraud'] = fraud_df['is_fraud']     # add fraud column

        # Merge on cc_num
        merged_df = transaction_df.merge(customer_df, how='left', on='cc_num')

        # clean up
        merged_df.drop_duplicates(inplace=True)
        merged_df.dropna(inplace=True)

        return merged_df

    ############## Just return data in right size / type ##################
    def describe(self, df):
        return {
            "number_of_records": len(df),
            "number_of_columns": df.shape[1],
            "feature_names": df.columns.tolist(),
            "number_missing_values": df.isnull().sum().sum(),
            "column_data_types": df.dtypes.astype(str).tolist()
        }