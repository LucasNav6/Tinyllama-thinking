import asyncio

class AgentStreamLogger:
    def __init__(self, agent):
        self.agent = agent

    async def stream(self, stream_func, *args, **kwargs):
        full_response = []

        async for chunk in stream_func(*args, **kwargs):
            prev_full_response_str = ''.join(full_response)
            prev_full_response_str_len = len(prev_full_response_str)
            new_text = chunk[prev_full_response_str_len:]
            full_response.append(new_text)
            print(new_text, end="", flush=True)
