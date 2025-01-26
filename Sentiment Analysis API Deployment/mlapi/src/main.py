from contextlib import AsyncExitStack
import sys
import os
from fastapi import FastAPI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sentiment_predict import lifespan, sub_application_sentiment_predict


async def main_lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        # Manage the lifecycle of sub_app
        await stack.enter_async_context(lifespan(sub_application_sentiment_predict))
        yield


app = FastAPI(lifespan=main_lifespan)


app.mount("/project", sub_application_sentiment_predict)
