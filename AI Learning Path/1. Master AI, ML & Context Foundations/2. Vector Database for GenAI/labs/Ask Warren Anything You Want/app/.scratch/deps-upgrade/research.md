# Dependency Upgrade & Docker Image Size Research

Scope: `app/streamlit_app/app.py`, `app/streamlit_app/preload_db.py`, `app/Dockerfile`, `app/requirements.txt`.

## Step 0 — Confirmed API surface (read from source)

`streamlit_app/preload_db.py`:
- `lancedb.connect(DB_URI)`, `db.table_names()`, `db.drop_table(TABLE_NAME)`, `db.create_table(TABLE_NAME, schema=Metadata)`, `table.add(chunks)`
- `from lancedb.embeddings import get_registry`; `get_registry().get("sentence-transformers").create(name="all-MiniLM-L6-v2")`
- `from lancedb.pydantic import LanceModel, Vector`; `Vector(model.ndims())`, `model.SourceField()`, `model.VectorField()`
- `from pypdf import PdfReader`; `PdfReader(path).pages[i].extract_text()`

`streamlit_app/app.py`:
- `lancedb.connect()`, `db.table_names()`, `db.open_table()`, `table.search(query).limit(3).to_pandas()` — result consumed via `row['year']`, `row['source']`, `row['_distance']`, `row['text']` (iterrows dict-like access)
- Streamlit: `st.set_page_config`, `st.tabs`, `st.session_state`, `st.progress(...).progress()/.empty()`, `st.text_input`, `st.download_button`, `st.selectbox`, `st.rerun()`, `st.balloons()`, `st.spinner`, `st.columns`, `st.metric`

**scikit-learn and plotly**: grep confirms neither `sklearn` nor `plotly` is imported anywhere in `streamlit_app/`. Confirmed dead direct deps (see §2 for the transitive-dependency caveat).

---

## 1. Major-version upgrade safety

### lancedb (0.38.0 → latest)
- PyPI JSON (`https://pypi.org/pypi/lancedb/json`) shows **0.38.0 is current latest** as of this research (2026-09-06). No newer version to bump to.
- Checked all GitHub releases (`https://github.com/lancedb/lancedb/releases`) for "Breaking Changes" sections back through v0.32–v0.38: all breaking-change entries concern `Permutation.with_format`, node.js embedding config keying, branch/merge naming, pydantic v2 requirement enforcement, and table-existence manifest semantics — **none touch** `connect`, `table_names`, `create_table`/`open_table`, `search().limit().to_pandas()` (`_distance` column), `embeddings.get_registry()`, or `pydantic.LanceModel`/`Vector`. The 0.38.0 note "refactor(python): require pydantic v2" (PR #3990) is already satisfied since the schema code uses `LanceModel` from lancedb's own pydantic v2-based module.
- Source: https://github.com/lancedb/lancedb/releases (tags v0.38.0, v0.37.1, v0.33.0, python-v0.36.0, etc.)
- **Verdict: no upgrade needed (already latest); safe to keep pinned at 0.38.0.**

### pypdf 4.1.0 → 6.x
- PyPI JSON: latest is **6.17.0**.
- Changelogs (`https://pypdf.readthedocs.io/en/5.0.0/meta/CHANGELOG.html`, `.../6.6.0/meta/CHANGELOG.html`): the PyPDF2→pypdf rename/namespace consolidation happened at **pypdf 2.0.0** (well before 4.1.0), so there is no additional rename between 4.x and 6.x. Breaking changes found in 4.x/5.x releases are: dropping Python 3.6 support (4.0.0), dropping Python 3.7 support (5.0.0), and removal of the already-deprecated `PdfMerger`/`AnnotationBuilder` legacy aliases (5.0.0, PR #2813). `PdfReader` and `.pages[i].extract_text()` are not renamed or signature-broken across 4→6; `extract_text()` has only received internal accuracy/whitespace fixes, not API changes.
- Source: https://pypdf.readthedocs.io/en/5.0.0/meta/CHANGELOG.html, https://pypdf.readthedocs.io/en/6.6.0/meta/CHANGELOG.html, PyPI JSON `https://pypi.org/pypi/pypdf/json`.
- **Verdict: safe to bump to 6.17.0.**

### streamlit 1.32.2 → latest 1.6x
- PyPI JSON: latest is **1.63.0**.
- Checked Streamlit's official yearly release notes (`https://docs.streamlit.io/develop/quick-reference/release-notes/2024`, 2025, 2026) for the exact APIs in use:
  - `st.rerun`: only bug fixes (1.41.0 raises on invalid `scope` arg — not used here). Code already uses `st.rerun()` (not deprecated `st.experimental_rerun()`), which remains the stable API.
  - `st.progress`: bug fix only (1.31.0, float precision >1.0). `.progress()`/`.empty()` methods unaffected.
  - `st.tabs`: 1.38.0 changed internal block-child handling to avoid visual artifacts — not an API signature break.
  - `st.session_state`: 1.36.0 added `None`-value support for nullable widgets — additive, not breaking.
  - `st.download_button`, `st.text_input`, `st.selectbox`, `st.balloons`: only additive features/bug fixes found (e.g. `st.text_input` no-rerun-on-unchanged-submit fix in 1.41.0; `st.selectbox` shallow-copy of options in 1.38.0) — no removed/renamed parameters affecting current usage.
- Source: https://docs.streamlit.io/develop/quick-reference/release-notes/2024, 2025, 2026; PyPI JSON `https://pypi.org/pypi/streamlit/json`.
- **Verdict: safe to bump to 1.63.0.**

### pandas 2.2.1 → latest 3.x
- PyPI JSON: latest is **3.0.5** (3.0.0 released 2026-01-21 per pandas official whatsnew page).
- Official pandas 3.0 release notes (`https://pandas.pydata.org/docs/whatsnew/v3.0.0.html`, pandas.pydata.org blog "Pandas 3.0 Released!"): two headline breaking changes:
  1. **Copy-on-Write (CoW) is now the default and only mode** — no opt-out. Breaks chained assignment (`df[col][row] = value`) patterns.
  2. **Default string dtype**: string columns are now inferred as a PyArrow-backed `str` dtype instead of numpy `object` dtype.
- Relevance to this codebase: `results = table.search(query).limit(3).to_pandas()` is read-only — the code only reads (`row['year']`, `row['source']`, `row['_distance']`, `row['text']`, `.strip()`, `:.4f}` formatting) via `.iterrows()`, never mutates the DataFrame or does chained assignment. `.strip()` on a string works identically whether the underlying dtype is numpy object or the new arrow-backed `str` dtype — no `dtype == object` checks exist in the code. `df_len = len(table.to_pandas())` is likewise unaffected by dtype changes.
- **Verdict: safe to bump to 3.0.5** for this specific read-only usage pattern; flagged as low-risk but worth a smoke test of the search results rendering after upgrade.
- Source: https://pandas.pydata.org/docs/whatsnew/v3.0.0.html, https://pandas.pydata.org/community/blog/pandas-3.0.html, PyPI JSON `https://pypi.org/pypi/pandas/json`.

---

## 2. scikit-learn and plotly — safe to delete?

- Grep confirms **plotly and scikit-learn are not imported** anywhere in `streamlit_app/`.
- **plotly**: Checked PyPI JSON `requires_dist` for `lancedb` (0.38.0), `streamlit` (1.63.0), and `sentence-transformers` (6.0.1) — plotly appears **only as an optional extra** of streamlit (`plotly>=4.0.0; extra == "charts"`), which is not installed since `requirements.txt` doesn't request `streamlit[charts]`. **plotly is fully removable with zero transitive re-install.**
  - Source: PyPI JSON `https://pypi.org/pypi/streamlit/json` → `info.requires_dist`.
- **scikit-learn**: Checked `sentence-transformers` PyPI JSON `requires_dist`: it lists `scikit-learn>=1.1.0` as a **core (non-extra) dependency**, not optional. `lancedb`'s own `requires_dist` never lists scikit-learn directly.
  - **Consequence: removing `scikit-learn` from `requirements.txt` will NOT remove it from the installed image** as long as `sentence-transformers` (pulled in by the LanceDB `sentence-transformers` embedding registry entry) stays a dependency — pip will silently re-resolve and install it transitively. It can be dropped from the explicit pin list (no direct import), but it will still land in site-packages (~8-9MB wheel, not the dominant cost) unless the embedding backend itself is swapped away from `sentence-transformers` (see §3).
  - Source: PyPI JSON `https://pypi.org/pypi/sentence-transformers/json` → `info.requires_dist` (`'scikit-learn>=1.1.0'`).
- **Verdict**: plotly → delete outright, zero side effects. scikit-learn → remove the explicit pin (it's dead weight to pin directly), but it is not eliminated from the image unless sentence-transformers is also removed.

---

## 3. Shrinking the sentence-transformers/torch footprint

### Does LanceDB have a built-in fastembed registry entry?
- Directory listing of `lancedb/python/python/lancedb/embeddings/` on GitHub main (`https://api.github.com/repos/lancedb/lancedb/contents/python/python/lancedb/embeddings`) shows these files: `__init__.py, base.py, bedrock.py, cohere.py, colpali.py, gemini_text.py, gte.py, gte_mlx_model.py, imagebind.py, instructor.py, jinaai.py, ollama.py, open_clip.py, openai.py, registry.py, sentence_transformers.py, siglip.py, transformers.py, utils.py, voyageai.py, watsonx.py`.
- **There is no `fastembed.py` and no fastembed-backed registry entry in LanceDB.** LanceDB's `sentence_transformers.py` registers only the `"sentence-transformers"` key (confirmed by reading the file: `@register("sentence-transformers")` → class `SentenceTransformerEmbeddings`, default model name `"all-MiniLM-L6-v2"`, `device="cpu"`, uses the `sentence-transformers` package internally). `gte.py` uses ONNX via `onnxruntime` directly but only for the GTE model family, not MiniLM/fastembed.
  - Source: https://api.github.com/repos/lancedb/lancedb/contents/python/python/lancedb/embeddings (file listing), https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/embeddings/sentence_transformers.py (read directly).
- **Conclusion: fastembed is NOT a registered LanceDB embedding function out of the box.** Using it would require writing a small custom `EmbeddingFunction` subclass (LanceDB's documented "Custom Embedding Functions" pattern, `@register("fastembed-minilm")` style) rather than a one-line `get_registry().get("fastembed")...` swap. This is more than a "name change" — it is a real code addition (~15-20 lines) in `preload_db.py`, though the resulting `LanceModel`/`Vector(model.ndims())`/`SourceField()`/`VectorField()` schema usage is unchanged since custom embedding functions implement the same `TextEmbeddingFunction` interface.

### Does fastembed have an all-MiniLM-L6-v2 model, and is it numerically identical?
- fastembed's supported-models list (`https://qdrant.github.io/fastembed/examples/Supported_Models/`) includes `sentence-transformers/all-MiniLM-L6-v2` as a distinct, **non-quantized** entry (fastembed denotes quantized variants with a `-Q` suffix, e.g. `BAAI/bge-small-en-v1.5-Q`; `all-MiniLM-L6-v2` has no such suffix).
- The underlying ONNX export is published at `https://huggingface.co/Qdrant/all-MiniLM-L6-v2-onnx` — described as "an ONNX port of sentence-transformers/all-MiniLM-L6-v2," fp32, not quantized.
- **Caveat / flag for the numeric-identity constraint**: ONNX export + a different inference runtime (onnxruntime vs. PyTorch) can still introduce small floating-point differences from operator-implementation/opset differences and from tokenizer/pooling implementation details reimplemented in fastembed rather than reusing sentence-transformers' Python pooling code, even when weights and architecture are unchanged and no quantization is applied. This is **very unlikely to change search *results* qualitatively** (same model, same 384-dim space, cosine/L2 relative ordering preserved) but the exact `_distance` floating-point values shown in the UI (`f"{row['_distance']:.4f}"`) could differ in the last 1-2 decimal digits from what the current sentence-transformers-based version currently produces. This should be flagged to the project owner as the one place where "identical vectors" is not literally guaranteed, only "functionally equivalent search behavior."
  - Source: https://qdrant.github.io/fastembed/examples/Supported_Models/, https://huggingface.co/Qdrant/all-MiniLM-L6-v2-onnx

### Exact code change needed if switching to fastembed
- `preload_db.py` would need: `pip install fastembed`, then either (a) use LanceDB's `TextEmbeddingFunction` custom-registration pattern documented at https://lancedb.com/documentation/embeddings/custom_embedding_function/ to wrap `fastembed.TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")`, registering it under a custom key (e.g. `@register("fastembed")`), or (b) call fastembed directly and populate the `vector` field manually without going through LanceDB's `SourceField()`/`VectorField()` embedding-function machinery (bypasses the automatic embed-on-`table.add()` behavior, which is a bigger behavioral change than the current code relies on). **Option (a) preserves the `model.SourceField()`/`model.VectorField()`/`Vector(model.ndims())` pattern unchanged** — only the `get_registry().get("sentence-transformers")` line changes to point at the new custom class.

### Package size comparison (PyPI JSON `files[].size`, linux x86_64 wheels)
| Package | Version | Wheel | Size |
|---|---|---|---|
| torch (default PyPI, CUDA-bundled) | 2.14.0 | `manylinux_2_28_x86_64` | **554.6 MB** |
| torch (PyTorch CPU-only index) | 2.6.0 | `linux_x86_64+cpu` | **178.7 MB** (confirmed via `curl -sI` Content-Length on `download.pytorch.org/whl/cpu`) |
| onnxruntime | 1.29.0 | `manylinux_2_28_x86_64` | 23.1 MB |
| fastembed | 0.8.0 | `py3-none-any` (pure Python wrapper) | 0.1 MB |
| scikit-learn | 1.9.0 | `manylinux_2_28_x86_64` | 9.1 MB |
| transformers | 5.16.1 | `py3-none-any` | 12.1 MB |

- **Default PyPI torch also pulls CUDA runtime packages as required (non-optional) dependencies** — confirmed via `https://pypi.org/pypi/torch/json` → `info.requires_dist`: `cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.3`, `nvidia-cudnn-cu13`, `nvidia-cusparselt-cu13`, `nvidia-nccl-cu13`, `nvidia-nvshmem-cu13`, `triton~=3.8.0` (all `platform_system == "Linux"`, unconditional on GPU presence). These packages alone commonly add 1.5-2.5 GB to a Linux image and are completely unused for CPU-only inference. **This is almost certainly the single largest contributor to the current 10.98 GB image size**, more so than the base torch wheel itself.
- fastembed + onnxruntime path: **~23 MB total** (onnxruntime) vs. torch CPU-only at **~179 MB**, vs. default torch+CUDA deps at **~2-3 GB effective install size**. Switching to fastembed is the single biggest lever available; CPU-only torch index is a much smaller, zero-code-risk fallback.

### CPU-only torch install (fallback if not switching to fastembed)
- Confirmed via PyTorch's own `pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu` command scraped from https://pytorch.org/get-started/locally/ (official "Get Started Locally" selector output; `pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu`).
- Exact Dockerfile syntax to add:
  ```dockerfile
  RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu torch
  ```
  (or `--index-url` instead of `--extra-index-url` if torch is installed in its own `pip install` step before other requirements, to avoid pip resolving other packages against the CPU-only index only). Since `sentence-transformers` pulls in `torch` as a dependency without pinning to a specific index, the safest approach is to install `torch` explicitly from the CPU index **before** `pip install -r requirements.txt`, so pip's dependency resolver sees it already satisfied and does not fall back to the default PyPI (CUDA) wheel.
  - Source: https://pytorch.org/get-started/locally/ (official install matrix/command generator).

---

## 4. Recommendation

**Final pins (`requirements.txt`):**
```
lancedb==0.38.0
pypdf==6.17.0
sentence-transformers==6.0.1   # only if staying on sentence-transformers backend; drop entirely if switching to fastembed
pandas==3.0.5
streamlit==1.63.0
fastembed==0.8.0               # if switching embedding backend (recommended)
```
Remove entirely: `scikit-learn`, `plotly` (neither imported; plotly has zero transitive path back in; scikit-learn only comes back if `sentence-transformers` stays).

**Decision: switch to fastembed for the embedding backend** (bigger win, small code change) as the primary recommendation, since the project owner explicitly said a backend-switch code change is acceptable as long as the model/dims/UI behavior are preserved. If the team wants zero code risk, the fallback is CPU-only torch via the PyTorch wheel index — much simpler but leaves ~180MB+ of torch plus ~12MB transformers plus ~9MB scikit-learn in the image instead of ~23MB total for onnxruntime+fastembed.

**Exact changes if switching to fastembed:**
- `requirements.txt`: remove `sentence-transformers`, `scikit-learn`, `plotly`; add `fastembed==0.8.0`.
- `streamlit_app/preload_db.py`:
  - Replace `from lancedb.embeddings import get_registry` usage: register a small custom `TextEmbeddingFunction` wrapping `fastembed.TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")` per LanceDB's documented custom-embedding-function pattern (https://lancedb.com/documentation/embeddings/custom_embedding_function/), then call `get_registry().get("<custom-name>").create()` in its place.
  - No change needed to `LanceModel`, `Vector(model.ndims())`, `model.SourceField()`, `model.VectorField()`, `table.add(chunks)` — the custom function implements the same interface.
- `streamlit_app/app.py`: **no changes needed** — `table.search(query).limit(3).to_pandas()` and the `_distance`/`text`/`year`/`source` column access are all LanceDB-table-level APIs, agnostic to which embedding function produced the vectors.
- Flag to project owner: fastembed's ONNX export of `all-MiniLM-L6-v2` is unquantized (same weights/architecture) but run through a different inference engine/tokenizer pooling path than sentence-transformers' PyTorch path, so **`_distance` values may differ in the last few decimal digits** from the current output; search *rankings* should remain effectively the same, but this is not a byte-for-byte numerical identity guarantee.

**Exact changes if instead keeping sentence-transformers (fallback, no code change):**
- `Dockerfile`: add, before `pip install -r requirements.txt`:
  ```dockerfile
  RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu torch
  ```
- `requirements.txt`: bump `sentence-transformers` to `6.0.1`, drop the explicit `scikit-learn`/`plotly` pins (scikit-learn will still be installed transitively via sentence-transformers, but at only ~9MB it's a rounding error compared to the torch CUDA deps this avoids).
- Bump `pypdf` to `6.17.0`, `streamlit` to `1.63.0`, `pandas` to `3.0.5`, keep `lancedb` at `0.38.0` (confirmed latest).

Either path removes plotly outright and eliminates the multi-GB CUDA dependency chain (`cuda-toolkit`, `nvidia-cudnn-cu13`, `nvidia-nccl-cu13`, `triton`, etc.) that default PyPI `torch` pulls in unconditionally on Linux — this CUDA chain, not the base torch wheel, is the primary reason for the current 10.98GB image size.
