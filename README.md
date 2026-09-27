

### POST /predict

Accepts customer information and returns churn prediction and probability.

Example request:

```json
{
  "tenure_months": 12,
  "support_tickets": 2,
  "monthly_spend_inr": 1000,
  "last_login_days": 5,
  "plan_type": "Basic"
}
```

Example response:

```json
{
  "prediction": 0,
  "churn_probability": 0.23,
  "result": "Customer likely to stay"
}
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

API documentation:

```text
http://localhost:8000/docs
```

## Docker

Build:

```bash
docker build -t customer-churn-api .
```

Run:

```bash
docker run -p 8000:8000 customer-churn-api
```

## Unit Testing

Run:

```bash
pytest test_main.py
```

Tests validate request validation, HTTP response codes, prediction output and response schema.

## Project Files

- `main.py` - FastAPI REST API
- `champion_churn_model.joblib` - trained ML model
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration
- `test_main.py` - unit tests
- `README.md` - project documentation

## Technology Stack

Python, FastAPI, Pandas, Scikit-learn, Joblib, Pydantic, Pytest and Docker.

## End-to-End Flow

Customer Data → FastAPI → Pydantic Validation → ML Model → Prediction Probability → JSON Response

## Author

Customer Churn Prediction Capstone Project
