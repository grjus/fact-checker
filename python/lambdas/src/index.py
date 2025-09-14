from agents import claim_verification_agent, claim_extraction_agent
from mappers import claims_to_str
from schemas import Claims


def handler(summary: str):
    claims = claim_extraction_agent.structured_output(Claims, summary)
    verified_claims = claim_verification_agent(claims_to_str(claims))
