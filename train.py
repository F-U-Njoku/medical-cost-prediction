# Import libraries
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

max_depth=5
n_estimators=400
dv = DictVectorizer(sparse=False)
output_file = f"model_{max_depth}_{n_estimators}.bin"

df = pd.read_csv("./Data/insurance.csv")

X = dv.fit_transform(df.drop(columns=["charges"]).to_dict(orient='records'))
y = np.log1p(df.charges)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

def train(X_train, y_train, n_estimators=n_estimators, max_depth=max_depth):
    
    rf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    rf.fit(X_train, y_train)

    return dv, rf

if __name__ == "__main__":
    print("Training final model.....")
    _, model = train(X_train, y_train)

    y_pred = model.predict(X_val)
    rmse = root_mean_squared_error(y_val, y_pred)
    print(f"Final model has RMSE of {round(rmse, 4)}")

    with open(output_file, "wb") as f_out:
        pickle.dump((dv, model), f_out)
    print(f"Final DictVectorizer and model saved as {output_file}")