import os
import json
from strands import tool

from ssm_client import get_secret
from serper_client import claims_search_tool as cst

SECRET_NAME = os.getenv("SECRET_NAME")


@tool
def search_tool(claims: list[str]) -> str:
    """Search for evidence about each claim."""
    secret = get_secret(SECRET_NAME)
    results = cst(claims, secret.GOOGLE_SEARCH)
    output = [each.model_dump() for each in results]
    return json.dumps(output)

