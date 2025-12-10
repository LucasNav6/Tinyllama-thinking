from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Adjust the system path to include the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger.logger import logger

# Define the model name
MODEL_NAME = 'tinyllama:latest'

logger.info(f"{os.environ.get('OLLAMA_URL')}, Model: {MODEL_NAME}")

# Initialize the Ollama model with the specified provider URL
ollama_model = OpenAIChatModel(
    model_name=MODEL_NAME,
    provider=OllamaProvider(base_url=os.environ.get('OLLAMA_URL')),  
)

# Create an agent using the Ollama model
agent = Agent(ollama_model)