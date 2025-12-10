import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planner.agent import PlannerAgent

from dotenv import load_dotenv
load_dotenv()

def answer_question(question):    
    planner_agent = PlannerAgent()
    plan = planner_agent.create_plan(question)
    return plan    

if __name__ == "__main__":
    sample_question = "What is the capital of France?"
    answer = answer_question(sample_question)
    print(f"Q: {sample_question}\nA: {answer}")