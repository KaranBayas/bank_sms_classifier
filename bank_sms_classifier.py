from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
import joblib
import traceback

# ---------------- LOAD MODEL ----------------
try:
    model = joblib.load("bank_sms_classifier.pkl")
except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

# ---------------- SCHEMA ----------------
class Text(BaseModel):
    sms: Annotated[
        str,
        Field(
            ...,
            description="Bank SMS to classify",
            min_length=1,
            max_length=1000
        )
    ]

# ---------------- APP ----------------
app = FastAPI(title="Bank SMS Classifier API")

# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {
        "message": "API is running",
        "status": True
    }

# ---------------- PREDICT ----------------
@app.post("/predict")
def predict(data: Text):
    try:
        # ✅ Extract string from Pydantic model
        sms_text = data.sms.strip().lower()

        if not sms_text:
            raise HTTPException(status_code=400, detail="SMS cannot be empty")

        # ✅ Pipeline expects list
        prediction = model.predict([sms_text])[0]

        # ✅ Optional probability (if supported)
        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = float(max(model.predict_proba([sms_text])[0]))

        # ✅ Clean response
        return {
            "success": True,
            "input": sms_text,
            "prediction": str(prediction),
            "confidence": confidence
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        # 🔥 Debug-friendly error (remove traceback in production)
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }