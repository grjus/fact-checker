import asyncio
import json

import requests

URL = "https://google.serper.dev/search"


async def claim_google_search(claim: str, api_key: str):
    payload = json.dumps({
        "q": claim
    })
    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", URL, headers=headers, data=payload).json()
    organic_results = response.get("organic", [])
    if not organic_results:
        return {
            "claim": claim,
            "search_results": "No results found."
        }

    return {
        "claim": claim,
        "search_results": "\n".join(each.get('snippet') for each in organic_results)
    }


async def batch_claim_google_search(claims: list[str], api_key: str):
    tasks = [claim_google_search(claim, api_key) for claim in claims]
    return await asyncio.gather(*tasks)


def claims_search_tool(claims: list[str], api_key: str):
    return asyncio.run(batch_claim_google_search(claims, api_key))
