# Bank SMS Classifier API

A FastAPI-based REST API that classifies bank transaction SMS messages into spending categories using a trained Machine Learning model.

## Features

- FastAPI REST API
- Bank SMS Classification using Machine Learning
- Input Validation with Pydantic
- Health Check Endpoint
- Confidence Score Support
- Easy Deployment on Render, Railway, Docker, or Cloud Platforms

## Project Structure

```text
.
├── main.py
├── bank_sms_classifier.pkl
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/bank-sms-classifier-api.git
cd bank-sms-classifier-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn main:app --reload
```

API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Endpoints

### Health Check

**GET /health**

Response:

```json
{
  "message": "API is running",
  "status": true
}
```

### Predict SMS Category

**POST /predict**

Request:

```json
{
  "sms": "debited rs 500 at amazon using your hdfc card"
}
```

Response:

```json
{
  "success": true,
  "input": "debited rs 500 at amazon using your hdfc card",
  "prediction": "shopping",
  "confidence": 0.94
}
```

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"sms\":\"credited salary of rs 45000 from company\"}"
```

## Machine Learning Model

The API loads a pre-trained model from:

```text
bank_sms_classifier.pkl
```

The model should be a Scikit-Learn Pipeline supporting:

```python
pipeline.predict(["sample sms"])
pipeline.predict_proba(["sample sms"])
```

## Error Handling

Example error response:

```json
{
  "detail": "SMS cannot be empty"
}
```

## Tech Stack

- Python
- FastAPI
- Pydantic
- Scikit-Learn
- Joblib
- Uvicorn

## Future Improvements

- Batch Predictions
- Authentication & API Keys
- Docker Support
- Cloud Deployment
- Merchant Name Extraction
- Transaction Amount Extraction
- Multi-language SMS Classification

## Author

**Karan Bayas**

B.Tech Computer Science Engineering, PICT Pune

Machine Learning & Software Development Enthusiast
