"""
Pydantic schemas for request/response validation.
Ensures type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, Field
from typing import Optional, Annotated


class PredictRequest(BaseModel):
    """Request model for SMS classification."""
    
    sms: Annotated[
        str,
        Field(
            ...,
            description="Bank SMS message to classify",
            min_length=1,
            max_length=1000,
            examples=["Your account has been debited with 500 INR"]
        )
    ]


class PredictResponse(BaseModel):
    """Response model for SMS classification prediction."""
    
    success: bool = Field(..., description="Whether prediction was successful")
    input: str = Field(..., description="The processed input SMS text")
    prediction: str = Field(..., description="Predicted SMS category")
    confidence: Optional[float] = Field(
        None, 
        description="Confidence score (0.0-1.0) if available",
        ge=0.0,
        le=1.0
    )


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    
    status: str = Field(..., description="API health status")
    message: str = Field(..., description="Status message")


class ErrorResponse(BaseModel):
    """Response model for error responses."""
    
    success: bool = Field(False, description="Indicates operation failed")
    error: str = Field(..., description="Error message")
