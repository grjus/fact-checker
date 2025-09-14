def to_reporter_prompt(summary: str, verified_claims: str) -> str:
    return f"<summary>{summary}</summary>\n\n<claims>{verified_claims}</claims>"
