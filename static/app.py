import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import logging



import openai
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel



# Set up logging
logging.basicConfig(level=logging.INFO)
# Initialize FastAPI app
app = FastAPI()

# Initialize your OpenAI API key
openai.api_key = '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'  # Replace with your actual API key

# Mount the static directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Define a Pydantic model for the request body
class GenerateRequest(BaseModel):
    prompt: str


# Define a Pydantic model for the response
class TextResponse(BaseModel):
    generated_text: str

