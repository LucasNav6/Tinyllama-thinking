from models.tinyllama_model import TinyLlamaModel

instruction = "Tu labor es unicamente crear un plan detallado paso a paso para responder preguntas de manera efectiva."

class PlannerAgent:
    def __init__(self):
        model = TinyLlamaModel()
        self.agent = model.build_agent(instruction=instruction)

    def create_plan(self, question: str) -> dict:
        plan = self.agent.run_sync("Armar un plan para: " + question)
        return plan.output