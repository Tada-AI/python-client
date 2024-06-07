from __future__ import annotations

from pydantic import Field, StrictFloat, StrictInt
from typing import Optional, Union
from typing import Optional

from tada_ai.models.api_model import ApiModel


class ChunkOptions(ApiModel):
    requested_min_word_count: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=50,
        description="Will attempt to keep the minimum chunk size to less than the provided amount. NOTE: This is not guaranteed. Please validate if your system requires a minimum or maximum size.",
    )
    requested_max_word_count: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=1500,
        description="Will attempt to keep the maximum chunk size to less than the provided amount. NOTE: This is not guaranteed. Please validate if your system requires a minimum or maximum size.",
    )
