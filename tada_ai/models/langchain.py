from typing import List

from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document

from tada_ai.client import TadaAIClient
from tada_ai.models.chunk_options import ChunkOptions
from tada_ai.models.reranker_options import RerankerOptions


class TadaAiRetriever(BaseRetriever):
    api_key: str | None = None
    chunks: ChunkOptions | None = None
    reranker: RerankerOptions | bool = True
    space_id: str | None = None

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        client = TadaAIClient(api_key=self.api_key)
        result = client.search(
            prompt=query,
            space_id=self.space_id,
            reranker=self.reranker,
            chunks=self.chunks,
        )

        return [Document(page_content=chunk.markdown) for chunk in result.chunks]
