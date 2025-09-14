from agents import claim_verification_agent, claim_extraction_agent, reporting_agent
from mappers import to_reporter_prompt
from schemas import ReporterOutput


def handler(summary: str):
    claims = claim_extraction_agent(summary)
    claims_content = claims.message.get("content", [])
    if not claims_content:
        raise ValueError("No claims extracted from the summary.")

    verified_claims = claim_verification_agent(claims_content[0].get("text"))
    verified_claims_content = verified_claims.message.get("content", [])
    if not verified_claims_content:
        raise ValueError("No verified claims returned from the verification agent.")

    report = reporting_agent.structured_output(
        ReporterOutput,
        to_reporter_prompt(summary, verified_claims_content[0].get("text")),
    )
    return report
