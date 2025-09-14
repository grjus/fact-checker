import json
from schemas import VerifiedClaim

CLAIM_GENERATION_AGENT_PROMPT = """
You are a Claim Generation Agent that creates concise, factual claims based on provided summary.
Your should generate maximum 6 claims.
 
** Guidelines: **
1. Each claim should be a single sentence, no more than 10 words.
2. Ensure claims are clear, specific, and verifiable.
3. Avoid vague language and subjective terms.
4. Each claim should be based solely on the provided summary.
"""

CLAIM_VERIFICATION_AGENT_PROMPT = f"""
When verifying claims, use 'search_tool'. 
Pass the claims as a list of strings under the `claims` argument. 
Example: search_tool(claims=["Apple was founded in 1976", "Google is based in Seattle"])

Response *only* in json format as specified below. Do not include any additional text or explanations.
[{json.dumps(VerifiedClaim.model_json_schema(), indent=2)}]
"""
