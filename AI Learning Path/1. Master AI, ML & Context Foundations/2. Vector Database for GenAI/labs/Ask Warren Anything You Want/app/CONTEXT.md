# Context

## Vector Database for GenAI app

Located at `AI Learning Path/1. Master AI, ML & Context Foundations/2. Vector Database for GenAI/app`. A small Streamlit + LanceDB RAG demo over Warren Buffett shareholder letters (PDFs), built for teaching purposes.

- **Embedding function**: the LanceDB registry entry (registered under the key `fastembed-minilm` in `streamlit_app/fastembed_minilm.py`) that turns letter-chunk text into 384-dim vectors. Backed by `fastembed`'s ONNX export of `sentence-transformers/all-MiniLM-L6-v2` — same weights and architecture as the original PyTorch model, run through a different (ONNX) inference engine. Must be imported by *any* process that opens the table (both `preload_db.py` and `app.py` import it), because LanceDB reconstructs the embedding function by its registered name at query time — omitting the import in a query-side process raises `KeyError` on `table.search()`.
- **`_distance`**: the per-result score LanceDB attaches to a search hit, shown in the UI. Since switching to the ONNX-backed embedding function, its value may differ from the old PyTorch-backed value in the last few decimal digits (different inference engine/tokenizer pooling path) — treat it as a relative ranking signal, not a byte-stable score.
