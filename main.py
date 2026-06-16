"""
Bank SMS Classifier REST API

This API provides endpoints to classify bank transaction SMS messages
into predefined categories using a trained machine learning model.

Author: [Your Name]
Version: 1.0.0
"""

import joblib
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

import config
from schemas import PredictRequest, PredictResponse, HealthResponse, ErrorResponse
from logger import logger

# ==================== MODEL INITIALIZATION ====================

_model = None


def load_model():
    """Load the trained ML model from disk."""
    global _model
    try:
        _model = joblib.load(str(config.MODEL_PATH))
        logger.info(f"Model loaded successfully from {config.MODEL_PATH}")
        return _model
    except FileNotFoundError as e:
        logger.error(f"Model file not found at {config.MODEL_PATH}")
        raise RuntimeError(
            f"Model file not found at {config.MODEL_PATH}. "
            "Please ensure the model file exists."
        )
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise RuntimeError(f"Model loading failed: {str(e)}")


def get_model():
    """Get the loaded model instance."""
    global _model
    if _model is None:
        load_model()
    return _model


# ==================== LIFESPAN EVENTS ====================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    # Startup: Load model
    load_model()
    logger.info("Application started")
    yield
    # Shutdown: Cleanup if needed
    logger.info("Application shutting down")


# ==================== APP INITIALIZATION ====================

app = FastAPI(
    title=config.API_TITLE,
    version=config.API_VERSION,
    description=config.API_DESCRIPTION,
    lifespan=lifespan
)


# ==================== ENDPOINTS ====================

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        HealthResponse: Status and message indicating API health
    """
    logger.debug("Health check requested")
    return HealthResponse(
        status="healthy",
        message="API is running and ready to serve requests"
    )


@app.post("/predict", response_model=PredictResponse)
async def predict(data: PredictRequest):
    """
    Classify a bank SMS message into a category.
    
    Args:
        data: Request containing SMS text to classify
        
    Returns:
        PredictResponse: Prediction result with confidence score
        
    Raises:
        HTTPException: If prediction fails or input is invalid
    """
    try:
        # Extract and normalize input
        sms_text = data.sms.strip().lower()
        logger.info(f"Processing SMS: {sms_text[:50]}...")
        
        # Get model and make prediction
        model = get_model()
        prediction = model.predict([sms_text])[0]
        
        # Calculate confidence if model supports predict_proba
        confidence = None
        if hasattr(model, "predict_proba"):
            try:
                probabilities = model.predict_proba([sms_text])[0]
                confidence = float(max(probabilities))
            except Exception as e:
                logger.warning(f"Could not calculate confidence: {str(e)}")
        
        logger.info(f"Prediction: {prediction} (confidence: {confidence})")
        
        return PredictResponse(
            success=True,
            input=sms_text,
            prediction=str(prediction),
            confidence=confidence
        )
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request. Please try again."
        )


# ==================== ERROR HANDLERS ====================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions with consistent error format."""
    logger.warning(f"HTTP Exception: {exc.detail}")
    return {
        "success": False,
        "error": exc.detail
    }


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {str(exc)}")
    return {
        "success": False,
        "error": "An unexpected error occurred. Please try again later."
    }


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level=config.LOG_LEVEL.lower()
    )
