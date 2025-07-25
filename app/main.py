from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Review Sentiment Analyzer")
app.include_router(router)