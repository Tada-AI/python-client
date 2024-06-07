from __future__ import annotations

from pydantic import Field, StrictBool, StrictFloat, StrictInt
from typing import Optional
from typing import Optional

from tada_ai.models.api_model import ApiModel


class RerankerOptions(ApiModel):
    use_reranker: Optional[StrictBool] = Field(
        default=True, description="Turns the reranker on or off."
    )
    top_n: Optional[StrictInt] = Field(
        default=10,
        description="The largest number of chunks to return from re-ranking",
    )
    threshold: Optional[StrictFloat] = Field(
        default=0.25, description="The minimum threshold for a chunk"
    )
