
############## fix Import Path ##################
import sys
import os
sys.path.append(os.path.abspath("."))      # add the project root so securebank

############## import##################
from securebank.modules.data.raw_data_handler import RawDataHandler     # import the class

############## file paths ##################
storage = "securebank/data_sources"        # folder where 3 raw files are
save = "securebank/data_output"            # output location for cleaned data if we decide to save

############## Handler ##################
handler = RawDataHandler(storage_path=storage, save_path=save)  # create the handler

############## Raw Data ##################
customer_info, transaction_info, fraud_info = handler.extract(
    "customer_release.csv",                 # customer info file
    "transactions_release.parquet",         # transaction file
    "fraud_release.json"                    # fraud labels file
)

############## transform and merge it ##################
cleaned_data = handler.transform(customer_info, transaction_info, fraud_info)  # merge it

############## Convert datetime columns ##################
cleaned_data = handler.convert_dates(cleaned_data)  # split date into components

############## print summary, types ##################
description = handler.describe(cleaned_data)        # summary infor function
print(description)
