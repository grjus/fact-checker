from pydantic import BaseModel, Field


class Claims(BaseModel):
    claims: list[str] = Field(...,
                              description="A list of concise, factual claims based on the provided summary. "
                                          "Each claim should be a single sentence, no more than 10 words.",
                              max_items=6)
