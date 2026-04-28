import os
from .env import load_dotenv

load_dotenv()

GROQ_API_KEY  = os.getenv("GROQ_API_KEY","")