import os
from dotenv import load_dotenv
from crewai import LLM

# Load environment variables
load_dotenv()

# Gemini LLM setup
GEMINI_LLM = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_tokens=2048,
)
