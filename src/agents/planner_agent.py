import asyncio
from models.tinyllama_model import TinyLlamaModel

instruction = "Tu labor es unicamente crear un plan detallado paso a paso para responder preguntas de manera efectiva."

class PlannerAgent:
    def __init__(self):
        model = TinyLlamaModel()
        self.agent = model.build_agent(instruction=instruction)
    
    async def redefinition_question_stream(self, question: str):
        instruction = "Responder la pregunta:"
        async with self.agent.run_stream(instruction + question) as response:
            async for text in response.stream_text():
                yield text

    async def create_plan_stream(self, question: str):
        async with self.agent.run_stream("Armar un plan para: " + question) as response:
            async for text in response.stream_text():
                yield text