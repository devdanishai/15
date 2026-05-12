import asyncio

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from llama_index.llms.ollama import Ollama


agent = FunctionAgent(
    tools=[],
    llm=Ollama(
        model="qwen3:32b",
        request_timeout=360.0,
    ),
    system_prompt="You are a concise assistant.Answer directly and briefly",
)


async def main():
    ctx = Context(agent)

    response1 = await agent.run(
        "My name is Logan",
        ctx=ctx
    )
    print(response1)

    response2 = await agent.run(
        "What is my name?",
        ctx=ctx
    )
    print(response2)


if __name__ == "__main__":
    asyncio.run(main())