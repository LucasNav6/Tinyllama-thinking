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
from config import MODEL_NAME


class TinyLlamaModel:
    def __init__(self):
        self.model: OpenAIChatModel = OpenAIChatModel(
            model_name=MODEL_NAME,
            provider=OllamaProvider(base_url=os.environ.get('OLLAMA_URL')),
        )

    def build_agent(self, instruction: str) -> Agent:
        logger.info(f"🤖 Building agent with instruction: {instruction}")
        return Agent(self.model, instructions=instruction)
