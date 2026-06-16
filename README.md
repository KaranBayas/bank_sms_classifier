# Bank SMS Classifier API

A production-ready REST API that classifies bank transaction SMS messages into spending categories using a trained machine learning model. Built with FastAPI for high performance and ease of deployment.

## 🎯 Project Overview

This project demonstrates building a professional ML-powered REST API that can classify incoming bank SMS notifications into predefined categories (e.g., debit, credit, fraud alert, promotional). The API includes proper error handling, input validation, logging, and is ready for deployment to cloud platforms.

## ✨ Features

- **FastAPI Framework**: Modern, fast Python web framework with automatic OpenAPI documentation
- **ML Classification**: Uses a pre-trained scikit-learn model for SMS categorization
- **Pydantic Validation**: Robust input validation with automatic documentation
- **Confidence Scoring**: Returns confidence levels for predictions when available
- **Health Monitoring**: Built-in health check endpoint for deployment verification
- **Structured Logging**: Comprehensive logging for debugging and monitoring
- **Error Handling**: Professional error responses without exposing sensitive debug info
- **Environment Configuration**: Configurable via environment variables
- **Production Ready**: Can be deployed to Render, Railway, Heroku, or Docker

## 📁 Project Structure

```
bank_sms_classifier/
├── main.py                          # FastAPI application and endpoints
├── config.py                        # Configuration and settings
├── schemas.py                       # Pydantic request/response models
├── logger.py                        # Logging configuration
├── bank_sms_classifier.pkl          # Pre-trained ML model
├── requirements.txt                 # Python dependencies
├── .env.example                     # Example environment variables
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/bank-sms-classifier.git
cd bank-sms-classifier
```

2. **Create a virtual environment:**
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment (optional):**
```bash
cp .env.example .env
# Edit .env if you need custom settings
```

### Running the API

**Development mode:**
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

**Production mode:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

## 📚 API Documentation

Once the API is running, you can access:

- **Swagger UI (Interactive)**: http://localhost:8000/docs
- **ReDoc (Alternative UI)**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 📡 Endpoints

### 1. Health Check

Check if the API is running and ready to serve requests.

**Request:**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "API is running and ready to serve requests"
}
```

**Status Code:** `200 OK`

---

### 2. Predict SMS Category

Classify a bank SMS message into a category.

**Request:**
```http
POST /predict
Content-Type: application/json

{
  "sms": "Your account has been debited with 500 INR at XYZ Merchant"
}
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "input": "your account has been debited with 500 inr at xyz merchant",
  "prediction": "debit_transaction",
  "confidence": 0.95
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "success": false,
  "error": "An error occurred while processing your request. Please try again."
}
```

**Validation Error (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "sms"],
      "msg": "String should have at least 1 character",
      "input": ""
    }
  ]
}
```

## 🔧 Configuration

Configuration can be managed via environment variables. Create a `.env` file:

```env
# API Configuration
LOG_LEVEL=INFO
MODEL_PATH=bank_sms_classifier.pkl
```

**Available Options:**
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR) - Default: INFO
- `MODEL_PATH`: Path to the pre-trained model file - Default: `bank_sms_classifier.pkl`

## 🛠 Technologies Used

- **FastAPI** (0.135.1): Modern web framework for building APIs
- **Uvicorn** (0.42.0): ASGI server for running FastAPI
- **Pydantic** (2.12.5): Data validation using Python type hints
- **Joblib** (1.5.3): For loading the ML model
- **Scikit-learn** (1.8.0): ML library used by the model
- **Python-dotenv** (1.0.1): Environment variable management

## 📊 Model Details

- **Type**: Classification model (likely Naive Bayes or similar)
- **Input**: SMS text message (lowercase, normalized)
- **Output**: Predicted category with optional confidence score
- **File**: `bank_sms_classifier.pkl`

### Input Constraints:
- Minimum length: 1 character
- Maximum length: 1000 characters
- Format: Text (will be normalized to lowercase)

## 🚢 Deployment

### Render.com
```bash
# Create render.yaml in project root
# Push to GitHub and connect to Render
```

### Railway.app
```bash
railway link
railway up
```

### Docker
```bash
docker build -t bank-sms-classifier .
docker run -p 8000:8000 bank-sms-classifier
```

### Local/VM
```bash
python main.py
```

## 📝 Logging

The application includes structured logging:
- All requests are logged with their processing details
- Errors are logged with context for debugging
- Log level can be configured via `LOG_LEVEL` environment variable

## 🔐 Security Notes

- Debug traceback is never exposed in API responses
- Model file path is configurable and not hardcoded
- Input validation prevents malformed requests
- Sensitive errors are logged but generic messages are returned to clients

## 🐛 Troubleshooting

**Model file not found:**
```
Ensure bank_sms_classifier.pkl exists in the project directory
or set the MODEL_PATH environment variable correctly
```

**Port 8000 already in use:**
```bash
uvicorn main:app --port 8001
```

**Import errors:**
```bash
pip install -r requirements.txt --upgrade
```

## 💡 Future Improvements

- [ ] Add user authentication and API keys
- [ ] Implement batch prediction endpoint for multiple SMS
- [ ] Add database to store prediction history
- [ ] Create model versioning system
- [ ] Add comprehensive unit and integration tests
- [ ] Implement caching for frequently predicted SMS
- [ ] Add Docker support for containerization
- [ ] Create admin dashboard for monitoring

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Your Name - Computer Science Student | github.com/your-username

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Last Updated:** June 2026

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
