import os
from crewai import Crew, Task, Agent
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["WATSONX_APIKEY"] = os.getenv("WATSONX_API")

# Parameters for LLM
parameters = {"decoding_method": "greedy", "max_new_tokens": 2048}

# Initialize Watsonx LLM instances
WATSONX_LLM = WatsonxLLM(
    model_id="meta-llama/llama-3-70b-instruct",
    url=os.getenv("WATSONX_URL"),
    params=parameters,
    project_id=os.getenv("WATSONX_PID"),
)
