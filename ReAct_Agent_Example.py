from agentscope.agent import ReActAgent, UserAgent
from agentscope.model import OllamaChatModel
from agentscope.formatter import OllamaChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.tool import Toolkit, execute_python_code, execute_shell_command
import asyncio

async def main():
    toolkit = Toolkit()
    toolkit.register_tool_function(execute_python_code)
    toolkit.register_tool_function(execute_shell_command)

    agent = ReActAgent(
        name="Friday",
        sys_prompt="You're a helpful assistant named Friday.",
        model=OllamaChatModel(
            model_name="gpt-oss",              # <-- ou "gpt-oss:latest"
            host="http://localhost:11434",
            stream=False,                      # começa estável
        ),
        memory=InMemoryMemory(),
        formatter=OllamaChatFormatter(),
        toolkit=toolkit,
    )

    user = UserAgent(name="user")

    msg = None
    while True:
        msg = await agent(msg)
        msg = await user(msg)
        if msg.get_text_content().strip().lower() == "exit":
            break

asyncio.run(main())
