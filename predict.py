# Import libraries
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split

max_depth=5
n_estimators=400
model_files = f"model_{max_depth}_{n_estimators}.bin"

applicant = {'age': 25,
             'sex':'male',
             'bmi': 45.54,
             'children':2,
             'smoker':'yes',
             'region':'southeast'} 	

with open(model_files, "rb") as f_in:
    dv, model = pickle.load(f_in)

def predict(applicant, dv=dv, model=model):
    
    pred = model.predict(dv.transform(applicant))
    actual_pred = np.expm1(pred)

    print("Applicant details: ", applicant)
    print(f"The predicted medical cost is ${round(actual_pred[0], 2)} yearly.")

    return actual_pred

if __name__ == "__main__":
    print("Calculating prediction.....")
    predict(applicant)