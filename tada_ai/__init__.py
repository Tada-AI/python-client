# coding: utf-8

# flake8: noqa

"""
    Tada AI API

    API for access Tada resources
"""  # noqa: E501


__version__ = "0.0.1"

from tada_ai.client import TadaAIClient

# import apis into sdk package
from tada_ai.api.default_api import DefaultApi

# import ApiClient
from tada_ai.exceptions import ApiException
from tada_ai.exceptions import ApiTypeError
from tada_ai.exceptions import ApiValueError
from tada_ai.exceptions import ApiKeyError
from tada_ai.exceptions import ApiAttributeError
from tada_ai.exceptions import ApiException

# import models into sdk package
from tada_ai.models.create_manual_space_input import CreateManualSpaceInput
from tada_ai.models.search_query_chunk_options_input import SearchQueryChunkOptionsInput
from tada_ai.models.search_query_input import SearchQueryInput
from tada_ai.models.search_query_reranker_options_input import (
    SearchQueryRerankerOptionsInput,
)
from tada_ai.models.search_record_chunk import SearchRecordChunk
from tada_ai.models.search_result_dto import SearchResultDto
from tada_ai.models.space import Space
from tada_ai.models.space_file import SpaceFile
from tada_ai.models.space_files_list_dto import SpaceFilesListDto
from tada_ai.models.space_list_dto import SpaceListDto
