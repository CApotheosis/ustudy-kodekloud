from lancedb.embeddings import register
from lancedb.embeddings.base import TextEmbeddingFunction
from lancedb.embeddings.utils import weak_lru
from fastembed import TextEmbedding


@register("fastembed-minilm")
class FastEmbedMiniLM(TextEmbeddingFunction):
    """all-MiniLM-L6-v2 via fastembed's ONNX runtime (no torch/CUDA needed)."""

    name: str = "sentence-transformers/all-MiniLM-L6-v2"

    def ndims(self):
        return 384

    @weak_lru(maxsize=1)
    def get_embedding_model(self):
        return TextEmbedding(model_name=self.name)

    def generate_embeddings(self, texts, *args, **kwargs):
        return [emb.tolist() for emb in self.get_embedding_model().embed(list(texts))]
