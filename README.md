# Customer Churn Prediction API

A Machine Learning REST API for predicting customer churn using FastAPI.

## Project Overview

This project predicts whether a customer is likely to churn based on customer usage and support information.

The trained machine learning model is exposed through a REST API using FastAPI and containerized using Docker.

## Input Features

- tenure_months
- support_tickets
- monthly_spend_inr
- last_login_days
- plan_type

## System Architecture

```text
Customer / Client
        |
        v
FastAPI REST API
        |
        v
Pydantic Input Validation
        |
        v
Trained Machine Learning Model
        |
        v
Prediction + Churn Probability
        |
        v
JSON Response
```

## API Endpoints

### GET /

Checks whether the API is running.

Example response:

```json
{
  "message": "Customer Churn Prediction API is running"
}
```

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

Open Swagger API documentation:

```text
http://localhost:8000/docs
```

## Docker

Build the Docker image:

```bash
docker build -t customer-churn-api .
```

Run the Docker container:

```bash
docker run -p 8000:8000 customer-churn-api
```

## Unit Testing

Run the tests:

```bash
pytest test_main.py
```

The tests validate:

- API response codes
- Input validation
- Prediction response
- Prediction schema
- Churn probability output

## Project Files

- `main.py` - FastAPI REST API
- `champion_churn_model.joblib` - trained machine learning model
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration
- `test_main.py` - unit tests
- `README.md` - project documentation

## Technology Stack

- Python
- FastAPI
- Pandas
- Scikit-learn
- Joblib
- Pydantic
- Pytest
- Docker

## End-to-End ML Flow

```text
Customer Data
      |
      v
FastAPI Endpoint
      |
      v
Input Validation
      |
      v
Machine Learning Model
      |
      v
Churn Prediction
      |
      v
Prediction Probability
      |
      v
JSON Response
```

## Model Output

The API returns:

- Prediction value
- Churn probability
- Human-readable prediction result

## Capstone Objective

The objective of this project is to package a trained machine learning model into a REST API that can receive JSON input and return real-time churn predictions.

## Author

Customer Churn Prediction Capstone Project
