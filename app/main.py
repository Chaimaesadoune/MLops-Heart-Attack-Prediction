from fastapi import FastAPI
import numpy as np
import joblib
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def predict(age: int, sex: int, cp: int, trtbps: int, chol: int, fbs: int, restecg: int,
            thalachh: int, exng: int, oldpeak: float, slp: int, caa: int, thall: int):
    features_to_predict = {
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trtbps': [trtbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalachh': [thalachh],
        'exng': [exng],
        'oldpeak': [oldpeak],
        'slp': [slp],
        'caa': [caa],
        'thall': [thall]
    }
    features_to_predict = np.array(
        [[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])
    model = joblib.load('./model.joblib')
    predicted_class = model.predict(features_to_predict.reshape(1, -1))
    return {"predicted_class": predicted_class.tolist()}


Instrumentator().instrument(app).expose(app)
