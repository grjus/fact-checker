import os

from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from strands.tools.executors import SequentialToolExecutor

from prompts import CLAIM_GENERATION_AGENT_PROMPT, CLAIM_VERIFICATION_AGENT_PROMPT
from serper_client import claims_search_tool as cst
from ssm_client import get_secret

os.environ["SECRET_NAME"] = "your-news/fact-checker"
SECRET_NAME = os.getenv("SECRET_NAME")


modelId = "eu.anthropic.claude-3-7-sonnet-20250219-v1:0"

inference_profile = {
    "max_tokens": 4096,
    "temperature": 0.0,
    "top_p": 1.0,
}
model = BedrockModel(model_id=modelId, **inference_profile)

claim_extraction_agent = Agent(
    system_prompt=CLAIM_GENERATION_AGENT_PROMPT,
    model=model,
    callback_handler=None,
    tools=[],
)

claim_verification_agent = Agent(
    system_prompt=CLAIM_VERIFICATION_AGENT_PROMPT,
    model=model,
    callback_handler=None,
    tool_executor=SequentialToolExecutor(),
    tools=["./tools/search_tool.py"],
)
