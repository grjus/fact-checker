import asyncio
import json

import requests

from python.lambdas.src.schemas import ClaimSearchResults, ClaimSearch

URL = "https://google.serper.dev/search"


async def claim_google_search(claim: str, api_key: str) -> ClaimSearchResults:
    payload = json.dumps({"q": claim})
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    response = requests.request("POST", URL, headers=headers, data=payload).json()
    organic_results = response.get("organic", [])
    if not organic_results:
        return ClaimSearchResults(claim=claim, search_results=[])
    return ClaimSearchResults(
        claim=claim,
        search_results=[
            ClaimSearch(snippet=each.get("snippet"), link=each.get("link"))
            for each in organic_results
        ],
    )


async def batch_claim_google_search(
    claims: list[str], api_key: str
) -> list[ClaimSearchResults]:
    tasks = [claim_google_search(claim, api_key) for claim in claims]
    return await asyncio.gather(*tasks)


def claims_search_tool(claims: list[str], api_key: str) -> list[ClaimSearchResults]:
    return asyncio.run(batch_claim_google_search(claims, api_key))
