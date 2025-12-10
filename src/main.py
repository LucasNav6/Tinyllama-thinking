import sys
import os
import asyncio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planner_agent import PlannerAgent
from utils.thinker.thinker import AgentStreamLogger

from dotenv import load_dotenv
load_dotenv()

async def answer_question_stream(question):
    # Paso 1: Redefinir la pregunta de una forma mejor planteada
    planner_agent = PlannerAgent()
    print(f"Q: {question}\nA: ", end="", flush=True)
    await AgentStreamLogger(planner_agent).stream(planner_agent.redefinition_question_stream, question)
    # planner_agent = PlannerAgent()
    # print(f"Q: {question}\nA: ", end="", flush=True)

    # # Usando el AgentStreamLogger con await para llamar al método async stream
    # await AgentStreamLogger(planner_agent).stream(planner_agent.create_plan_stream, question)

if __name__ == "__main__":
    sample_question = "Hola"
    asyncio.run(answer_question_stream(sample_question))