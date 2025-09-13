from strands import Agent
from strands.models.bedrock import BedrockModel

from prompts import CLAIM_GENERATION_AGENT_PROMPT

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
