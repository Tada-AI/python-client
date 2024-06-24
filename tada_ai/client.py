import os
from typing import Optional
import typing
import requests
from tada_ai.exceptions import ApiException
from tada_ai.models.chunk_options import ChunkOptions
from tada_ai.models.content_blocks import RootContentBlock
from tada_ai.models.search_query_input import SearchQueryInput
from tada_ai.models.reranker_options import (
    RerankerOptions,
)
from tada_ai.models.search_result import SearchResult
from tada_ai.models.space import Space
from tada_ai.models.space_file import SpaceFile
from tada_ai.models.space_files_list import SpaceFilesList
from tada_ai.models.space_list import SpaceList

DEFAULT_BASE_URL = "https://api.tadatoday.ai/api"

import io


class BaseService:
    def __init__(self, api_key: str, *, base_url: str):
        self.api_key = api_key
        self._base_url = base_url

    def _url(self, *path: str):
        return _join_url(self._base_url, *path)


class TadaAIClient(BaseService):
    def __init__(
        self, api_key: str | None = None, *, base_url: str = DEFAULT_BASE_URL
    ) -> None:
        api_key = (
            os.environ.get("TADA_AI_API_KEY", None) if api_key is None else api_key
        )
        if api_key is None:
            raise Exception(
                '"TADA_AI_API_KEY" not found in env. Either set the environment variable, or pass in the key manually'
            )

        return super().__init__(api_key, base_url=base_url)

    def search(
        self,
        prompt: str,
        *,
        space_id: str | None = None,
        reranker: RerankerOptions | bool = True,
        chunks: Optional[ChunkOptions] = None,
    ):
        url = self._url("search")

        if reranker == False:
            rerankerOptions = None
        elif reranker == True:
            rerankerOptions = RerankerOptions(use_reranker=True)
        else:
            rerankerOptions = reranker

        input = SearchQueryInput(
            prompt=prompt,
            space_id=space_id,
            reranker=rerankerOptions,
            chunk_options=chunks,
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        response = requests.post(
            url, json=input.model_dump(by_alias=True), headers=headers
        )
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return SearchResult.model_validate_json(response.text)

    @property
    def spaces(self):
        return SpaceService(self.api_key, base_url=self._base_url)

    @property
    def space_files(self):
        return SpaceFileService(self.api_key, base_url=self._base_url)


class SpaceFileService(BaseService):
    def get(self, space_file_id: str):
        url = self._url("space-files", space_file_id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return SpaceFile.model_validate_json(response.text)

    def list(self, space_id: str):
        url = self._url("spaces", space_id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return SpaceFilesList.model_validate_json(response.text)

    def create(self, space_id: str, file: typing.BinaryIO, path: str, mime_type: str):
        url = self._url("spaces", space_id, "files")
        headers = {"Authorization": f"ApiKey {self.api_key}"}
        files = {"file": (path, file, mime_type)}
        try:
            response = requests.post(url, headers=headers, files=files)
        except UnicodeDecodeError:
            raise Exception(
                "The file contains bytes, but was opened as text. Did you mean to do `open('my-file', 'rb')`?"
            )

        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return SpaceFile.model_validate_json(response.text)

    def content_blocks(self, space_file_id: str):
        url = self._url("space-files", space_file_id, "content-blocks")
        headers = {"Authorization": f"ApiKey {self.api_key}"}
        response = requests.get(url, headers=headers)

        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return RootContentBlock.model_validate_json(response.text)


class SpaceService(BaseService):
    def create(self, name: str):
        url = self._url("spaces")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        response = requests.post(url, json={"name": name}, headers=headers)
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return Space.model_validate_json(response.text)

    def get(self, space_id: str):
        url = self._url("spaces", space_id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return Space.model_validate_json(response.text)

    def list(self):
        url = self._url("spaces")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        print(url, headers)
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise ApiException.from_response(
                http_resp=response, body=response.text, data=None
            )

        return SpaceList.model_validate_json(response.text)


def _join_url(base_url: str, *path_items: str):
    if base_url.endswith("/"):
        base_url = base_url[:-1]
    path = [
        path_item[1:] if path_item.startswith("/") else path_item
        for path_item in path_items
    ]

    path.insert(0, base_url)
    return "/".join(path)
