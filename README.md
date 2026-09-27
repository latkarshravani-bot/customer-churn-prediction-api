# Customer Churn Prediction API

A production-ready Machine Learning REST API for predicting customer churn using FastAPI.

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

Client Application
        |
        v
FastAPI REST API
        |
        v
Input Validation using Pydantic
        |
        v
Trained ML Model
        |
        v
Prediction + Churn Probability
        |
        v
JSON Response

## API Endpoints

### GET /

Checks whether the API is running.

Example response:

```json
{
  "message": "Customer Churn Prediction API is running"
}
