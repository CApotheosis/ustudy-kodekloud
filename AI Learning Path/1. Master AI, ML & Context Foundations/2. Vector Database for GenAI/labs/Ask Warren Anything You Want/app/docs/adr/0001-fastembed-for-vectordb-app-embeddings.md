# Use fastembed (ONNX) instead of sentence-transformers for the Vector Database for GenAI app's embeddings

The app's Docker build was broken (`lancedb==0.9.0` had been yanked from PyPI); fixing that pin surfaced that the built image was 10.98GB. Investigation found the dominant cost wasn't LanceDB itself but `sentence-transformers`, which pulls in `torch`, which on Linux pulls in a full CUDA stack (`nvidia-*`, `triton`, ~5.3GB combined) unconditionally — even though this app only ever does CPU inference (`torch.cuda.is_available()` was confirmed `False`; no GPU is requested anywhere).

We considered installing `torch` from the CPU-only wheel index instead (`--index-url https://download.pytorch.org/whl/cpu`), which is a zero-code-change fix and shrinks torch from ~554MB+CUDA to ~179MB. We rejected it as the primary fix because it leaves ~180MB+ of torch, `transformers`, and `scikit-learn` in the image for one small model, when the same model is available through a much lighter path.

Instead we replaced LanceDB's built-in `"sentence-transformers"` embedding registry entry with a custom `TextEmbeddingFunction` (`streamlit_app/fastembed_minilm.py`, registered as `"fastembed-minilm"`) wrapping `fastembed`'s ONNX export of the same `sentence-transformers/all-MiniLM-L6-v2` model — same weights, same architecture, 384 dims, unquantized. This cut the image to 1.91GB (83% smaller) at the cost of a small code change instead of none.

**Consequences:**
- Both `preload_db.py` and `app.py` must import `fastembed_minilm` even where they don't call it directly, since LanceDB reconstructs an embedding function by its registered name at query time — the table itself only stores the name `"fastembed-minilm"`, not the class. Skipping the import in a query-side process raises `KeyError` on `table.search()`.
- The ONNX runtime may produce `_distance` values that differ from the old PyTorch path in the last few decimal digits (different inference engine and tokenizer pooling path). This is a cosmetic risk to the score shown in the UI, not a retrieval-quality risk — rankings are expected to hold since the weights and architecture are identical.
