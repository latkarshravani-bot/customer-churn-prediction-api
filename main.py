from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("champion_model.joblib")


class CustomerData(BaseModel):
    tenure_months: float
    support_tickets: float
    monthly_spend_inr: float
    last_login_days: float
    plan_type: str


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
def predict(data: CustomerData):

    input_data = pd.DataFrame([{
        "tenure_months": data.tenure_months,
        "support_tickets": data.support_tickets,
        "monthly_spend_inr": data.monthly_spend_inr,
        "last_login_days": data.last_login_days,
        "plan_type": data.plan_type
    }])

    prediction = int(model.predict(input_data)[0])

    probabilities = model.predict_proba(input_data)[0]

    return {
        "prediction": prediction,
        "churn_probability": float(probabilities[1]),
        "result": "Customer likely to churn" if prediction == 1 else "Customer likely to stay"
    }
