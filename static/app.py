import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import logging



import openai
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel





