# models.py

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    query: str


class AskResponse(BaseModel):
    answer: str
    sources: list
    confidence: float = Field(ge=0.0, le=1.0)
    
