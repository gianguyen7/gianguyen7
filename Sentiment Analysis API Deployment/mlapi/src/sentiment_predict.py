import logging
import os
from contextlib import asynccontextmanager
import json
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from typing import List
from redis import asyncio
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import hashlib

model_path = os.getenv(
    "MODEL_PATH",
    "/Users/gianguyen/Desktop/MIDS/DATASCI 255/project-pytorch-fastapi-giaknguyen/mlapi/distilbert-base-uncased-finetuned-sst2"
)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    device=-1,
    top_k=None,
)

logger = logging.getLogger(__name__)
REDIS_URL = os.getenv('REDIS_URL', "redis://localhost")
REDIS_PORT = os.getenv('REDIS_PORT', "6379")
REDIS_FULL_URL = f"{REDIS_URL}:{REDIS_PORT}/0"
# REDIS_FULL_URL = "redis://redis-server:6379/0"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # HOST_URL = os.environ.get("REDIS_URL", LOCAL_REDIS_URL)
    logger.debug(REDIS_FULL_URL)
    redis = asyncio.from_url(REDIS_FULL_URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache-project")

    yield


sub_application_sentiment_predict = FastAPI(lifespan=lifespan)


class SentimentRequest(BaseModel):
    text: List[str]


class Sentiment(BaseModel):
    label: str
    score: float


class SentimentResponse(BaseModel):
    predictions: List[List[dict]]


@sub_application_sentiment_predict.post(
    "/bulk-predict", response_model=SentimentResponse
)
@cache(expire=60)
async def predict(sentiments: SentimentRequest):
    return {
        "predictions": [
            [] if not text.strip() else classifier([text])[0]
            for text in sentiments.text
        ]
    }

@sub_application_sentiment_predict.get("/health")
async def health():
    return {"status": "healthy"}
