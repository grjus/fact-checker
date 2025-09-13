import os

from strands import Agent, tool
from strands.models.bedrock import BedrockModel

from prompts import CLAIM_GENERATION_AGENT_PROMPT, CLAIM_VERIFICATION_AGENT_PROMPT
from serper_client import claims_search_tool as cst
from ssm_client import get_secret

SECRET_NAME = os.getenv('SECRET_NAME')


@tool
def claims_search_tool(claims: list[str]):
    api_key = get_secret(SECRET_NAME)
    return cst(claims, api_key)


modelId = 'eu.anthropic.claude-3-7-sonnet-20250219-v1:0'

inference_profile = {
    "max_tokens": 4096,
    "temperature": 0.0,
    "top_p": 1.0,
    "top_k": 0,
}
model = BedrockModel(modelId=modelId, **inference_profile)

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
    tools=[claims_search_tool],
)
