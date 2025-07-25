from fastapi import APIRouter, Query
from typing import List, Optional

from .models import ReviewIn, ReviewOut
from .sentiment import SentimentAnalyzer
from .db import Database

router = APIRouter()
db = Database()

@router.post("/reviews", response_model=ReviewOut)
def create_review(review: ReviewIn):
    sentiment = SentimentAnalyzer.detect(review.text)
    saved = db.insert_review(review.text, sentiment)
    return ReviewOut(**saved)

@router.get("/reviews", response_model=List[ReviewOut])
def list_reviews(sentiment: Optional[str] = Query(None, description="Filter by sentiment")):
    rows = db.get_reviews(sentiment)
    return [ReviewOut(**dict(row)) for row in rows]