#!/usr/bin/env python3
from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
from openai_service import OpenAIService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


app = FastAPI()
items = []

# Initialize OpenAI service
openai_service = OpenAIService(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define request model
class FeedRequest(BaseModel):
    feedRequest: str

#operation to get the feed design
@app.post("/feed-design")
async def feed_design(request: FeedRequest):
    response = await openai_service.generate_feed_design(request.feedRequest)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 
    