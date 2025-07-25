from pydantic import BaseModel

class ReviewIn(BaseModel):
    text: str

class ReviewOut(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str