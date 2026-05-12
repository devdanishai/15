import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama


def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    print(f"Tool called with: {a}, {b}")
    return a * b


agent = FunctionAgent(
    tools=[multiply],
    llm=Ollama(
        model="qwen3:32b",
        request_timeout=360.0,
        context_window=8000,
    ),
    system_prompt=(
        "You are a calculator assistant. "
        "Always use the multiply tool for multiplication."
    ),
    verbose=True,   # important
)


async def main():
    response = await agent.run("What is 1234 * 4567?")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())