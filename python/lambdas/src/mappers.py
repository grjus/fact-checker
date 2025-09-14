from python.lambdas.src.schemas import Claims


def claims_to_str(claims: Claims) -> str:
    instruction = "Use 'claims_search_tool' to verify the following claims:\n"
    instruction += "\n".join(f"- {claim}" for claim in claims.claims)
    instruction += "\nProvide your response in the VerifiedClaims format."
    return instruction
