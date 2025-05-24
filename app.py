############## import ##################
from modules.model import Model
from flask import Flask, request, jsonify
############## Init flask app ##################
app = Flask(__name__)   #make my first flask web server...

############## prediction ##################
@app.route('/predict/', methods=['POST'])         # listen for POST to /predict/
def predict():
    try:
        # Get the JSON data from the request body
        input_data = request.get_json()           # parse incoming JSON

        prediction = Model.predict(input_data)    # call the model's predict function

        # Return the prediction result as JSON
        return jsonify({'prediction': prediction}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400    # return errors from jsonify

############## Run the Server ##################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # run on all for docker, go to port