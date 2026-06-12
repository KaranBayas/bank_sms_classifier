markdown # Bank SMS Classifier API  A FastAPI-based REST API that classifies bank transaction SMS messages into predefined spending categories using a trained Machine Learning model.  ## Features  - Fast and lightweight API built with FastAPI - ML-powered SMS classification - Input validation using Pydantic - Health check endpoint - Confidence score support (when model supports probabilities) - Ready for deployment on Render, Railway, Docker, or any cloud platform  ---  ## Project Structure  . ├── main.py ├── bank_sms_classifier.pkl ├── requirements.txt └── README.md  ---  ## Installation  ### 1. Clone the Repository  bash
git clone https://github.com/your-username/bank-sms-classifier-api.git
cd bank-sms-classifier-api
 ### 2. Create Virtual Environment bash
python -m venv venv
 Activate environment:  **Windows**bash
venv\Scripts\activate
 **Linux / macOS**bash
source venv/bin/activate
 ### 3. Install Dependencies bash
pip install -r requirements.txt
 ---  ## Run the API bash
uvicorn main:app --reload
 Server will start at: text
http://127.0.0.1:8000
 ---  ## API Documentation  Swagger UI: text
http://127.0.0.1:8000/docs
 ReDoc: text
http://127.0.0.1:8000/redoc
 ---  ## Endpoints  ### Health Check  **GET /health**  Response: json
{
  "message": "API is running",
  "status": true
}
 ---  ### Predict SMS Category  **POST /predict**  Request: json
{
  "sms": "debited rs 500 at amazon using your hdfc card"
}
 Response: json
{
  "success": true,
  "input": "debited rs 500 at amazon using your hdfc card",
  "prediction": "shopping",
  "confidence": 0.94
}
 ---  ## Example cURL Request bash
curl -X POST "http://127.0.0.1:8000/predict" 
-H "Content-Type: application/json" 
-d '{
  "sms":"credited salary of rs 45000 from company"
}'
 ---  ## Machine Learning Model  The API loads a pre-trained model from: text
bank_sms_classifier.pkl
 The model is expected to be a Scikit-Learn Pipeline that includes:  - Text preprocessing - TF-IDF Vectorization - Classification model  Example: python
pipeline.predict(["sample sms"])
pipeline.predict_proba(["sample sms"])
 ---  ## Error Handling  The API validates:  - Empty SMS messages - Invalid request payloads - Model prediction errors  Example: json
{
  "detail": "SMS cannot be empty"
}
 ---  ## Tech Stack  - Python - FastAPI - Pydantic - Scikit-Learn - Joblib - Uvicorn  ---  ## Future Improvements  - Batch SMS classification - Authentication and API keys - Docker support - Cloud deployment - Transaction amount extraction - Merchant name extraction - Multi-language SMS support  ---  ## Author  **Karan Bayas**  B.Tech Computer Science Engineering, PICT Pune  Machine Learning & Software Development Enthusiast
:::
