# Import libraries
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split

# Initialize Flask app
app = Flask('med_cost')

# Add health check endpoints
@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'OK', 'message': 'Medical Cost Prediction API is running'}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

# Load model
max_depth = 5
n_estimators = 400
model_files = f"model_{max_depth}_{n_estimators}.bin"

with open(model_files, "rb") as f_in:
    dv, model = pickle.load(f_in)

def make_prediction(applicant_data, dv=dv, model=model):
    """
    Makes prediction using the loaded model
    
    Parameters:
    applicant_data (dict): Dictionary containing applicant information
    dv: DictVectorizer instance
    model: Trained model instance
    
    Returns:
    float: Predicted medical cost
    """
    try:
        # Transform the input data
        X = dv.transform(applicant_data)
        
        # Make prediction
        pred = model.predict(X)
        
        # Transform prediction back to original scale
        actual_pred = np.expm1(pred)
        
        return actual_pred[0]
    
    except Exception as e:
        raise ValueError(f"Error making prediction: {str(e)}")

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    """
    API endpoint that receives JSON data and returns prediction
    """
    try:
        # Get JSON data from request
        applicant = request.get_json()
        
        if not applicant:
            return jsonify({"error": "No data provided"}), 400
        
        # Make prediction
        predicted_cost = make_prediction(applicant)
        
        # Format response
        result = {
            "predicted_medical_cost": round(predicted_cost, 2),
            "status": "success"
        }
        
        return jsonify(result)
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
