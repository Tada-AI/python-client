# coding: utf-8

# flake8: noqa

"""
    Tada AI API

    API for access Tada resources
"""  # noqa: E501


__version__ = "0.0.1"

from tada_ai.client import TadaAIClient


# import ApiClient
from tada_ai.exceptions import ApiError
from tada_ai.exceptions import ApiTypeError
from tada_ai.exceptions import ApiValueError
from tada_ai.exceptions import ApiKeyError
from tada_ai.exceptions import ApiAttributeError
from tada_ai.exceptions import ApiError

# import models into sdk package
from tada_ai.models.chunk_options import ChunkOptions
from tada_ai.models.search_query_input import SearchQueryInput
from tada_ai.models.reranker_options import (
    RerankerOptions,
)
from tada_ai.models.search_record_chunk import SearchRecordChunk
from tada_ai.models.search_result import SearchResult
from tada_ai.models.space import Space
from tada_ai.models.space_file import SpaceFile
from tada_ai.models.space_files_list import SpaceFilesList
from tada_ai.models.space_list import SpaceList
