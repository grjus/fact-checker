from typing import Optional

from pydantic import BaseModel, Field


class ClaimSearch(BaseModel):
    snippet: Optional[str] = Field(
        description="A brief snippet from the search result that is relevant to the claim.",
        default=None,
    )
    link: Optional[str] = Field(
        description="The URL of the search result.", default=None
    )


class FactCheckSecret(BaseModel):
    GOOGLE_SEARCH: str = Field(..., description="API key for Google Search service.")


class ClaimSearchResults(BaseModel):
    claim: str = Field(..., description="The original claim that was searched.")
    search_results: list[ClaimSearch] = Field(
        ..., description="A list of relevant search results used to verify the claim."
    )


class VerifiedClaim(BaseModel):
    claim: str = Field(..., description="The original claim to be verified.")
    is_true: bool = Field(
        ..., description="Indicates whether the claim is true or false."
    )
    confidence_level: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="A confidence score between 0 and 1 representing the certainty of the verification.",
    )
    tool_used: bool = Field(
        ...,
        description="Indicates whether the claims_search_tool was used to gather additional information for verification.",
    )
    search_results: list[ClaimSearch] | None = Field(
        None,
        description="Relevant search results used to verify the claim, if applicable.",
    )


class ReporterOutput(BaseModel):
    claim: list[VerifiedClaim] = Field(
        description="List of verified claims.", default=[]
    )
    summary: list[str] = Field(
        description="Concise summary of the fact-checking results.", default=[]
    )
