## Ask Warren Anything - VectorDB Semantic Search Demo

What You'll Explore
In this demo lab, you will explore a fully working Streamlit application that uses LanceDB (a vector database) to perform semantic search across 5 years of Warren Buffett's shareholder letters (2020-2024).

How It Works
PDF Ingestion: Reads 5 shareholder letters using pypdf
Text Chunking: Splits documents into 500-character chunks with 50-char overlap
Embeddings: Converts text to 384-dimensional vectors using all-MiniLM-L6-v2
Vector Storage: Stores embeddings in LanceDB with metadata (year, source)
Semantic Search: Finds relevant chunks by meaning, not keywords
You'll first understand the code, then build and run the app, and finally explore it hands-on!

---

Task 1: Understand the Application
Explore the Application Code
Before building the app, let's understand how each piece works. Browse through the source files to understand the architecture.

Key Files to Explore:

streamlit_app/preload_db.py - The data pipeline that reads PDFs, chunks text, generates embeddings, and stores them in LanceDB
streamlit_app/app.py - The Streamlit UI with document viewer, ingestion simulation, and semantic search
Dockerfile - Builds the containerized app with pre-loaded embeddings
requirements.txt - Dependencies: lancedb, pypdf, sentence-transformers, streamlit
share-holder-letters/ - 5 PDF files (2020-2024 Berkshire Hathaway letters)
Understanding preload_db.py - The Data Pipeline

```
Step 1: Read PDFs       → pypdf extracts text from each letter
Step 2: Chunk Text      → 500-char chunks with 50-char overlap
Step 3: Generate Embeds → all-MiniLM-L6-v2 (384 dimensions)
Step 4: Store in LanceDB → Table with year, source, text, vector
```

The LanceDB schema uses a Pydantic model with SourceField() and VectorField() decorators, allowing LanceDB to automatically handle embedding generation during insertion.

Understanding app.py - The Streamlit UI
Document Viewer Tab: Displays shareholder letters as embedded PDFs
Vector Search Tab: Simulates ingestion with a progress bar, then opens a free-text semantic search interface
Search Results: Shows matched text chunks with year, source file, and distance score
The search uses table.search(query).limit(3) which automatically embeds the query and finds the 3 most similar chunks using cosine distance.

Run this command to verify you've explored the files

```bash
cat /root/app/streamlit_app/preload_db.py && echo '---' && cat /root/app/streamlit_app/app.py && touch /tmp/task1_explored.txt && echo 'Task 1 Complete: Code explored!'
```

---

## Why LanceDB?

Embedded Vector Database
Unlike client-server databases (Pinecone, Weaviate), LanceDB runs embedded - no separate server needed!

Zero infrastructure: Just pip install lancedb
Local storage: Data lives on disk as Lance format files
Auto-embedding: Built-in integration with sentence-transformers
Schema-driven: Uses Pydantic models for type-safe data
The Embedding Pipeline in This App

```py
model = get_registry().get("sentence-transformers")
         .create(name="all-MiniLM-L6-v2")

class Metadata(LanceModel):
    year: int
    source: str
    text: str = model.SourceField()     # Auto-embed this field
    vector: Vector(384) = model.VectorField()  # Store here

table.add(chunks)  # Embedding happens automatically!
```

Key Insight: LanceDB handles embedding generation during table.add() and query embedding during table.search() - you just pass raw text!

---

## Task 2: Build and Run the Application

Build the Docker Container
The application is fully Dockerized. The Docker build process will:

Set up Python 3.10 environment
Install all dependencies (lancedb, sentence-transformers, streamlit, etc.)
Copy the Streamlit app and shareholder letter PDFs
Pre-load embeddings by running preload_db.py during build
Configure Streamlit to serve on port 8501
Note: The build step downloads the all-MiniLM-L6-v2 model (~80MB) and generates embeddings for all 5 letters. This takes a few minutes - that's why we pre-load during Docker build!

Step 1: Build the Docker Image

```bash
cd /root/app && docker build -t lancedb-quickstart .
```

Step 2: Run the Container

```bash
docker run -d --name warren-app -p 8501:8501 lancedb-quickstart
```

Step 3: Verify that the Container is Running

```bash
docker ps | grep warren-app
```

---

## How Semantic Search Works in This App

The Search Flow

```
User types: "What does Warren think about COVID?"
↓

1. Query → Embedding [0.12, 0.87, 0.34, ...] (384 dims)
   ↓
2. LanceDB finds nearest vectors (cosine distance)
   ↓
3. Returns top 3 matching text chunks with:
   - Year (2020, 2021, etc.)
   - Source file (2020ltr.pdf)
   - Distance score (lower = more similar)
     ↓
4. Streamlit renders results with source citations
```

Why This Is Powerful
Ask about "pandemic impact" → Finds COVID-19 discussion even if those exact words aren't used
Ask about "stock buybacks" → Finds paragraphs about share repurchases
Ask about "Charlie Munger" → Finds tribute and partnership mentions across years
The distance score tells you how semantically close a result is. Lower distance = closer meaning. Compare scores across different queries to see how confidence varies!

---

## Task 3: Explore the Application

Interact with the Streamlit App
Now that the app is running, open it in your browser and explore the full semantic search experience.

Access the app:

Click on the Streamlit App UI at the top of the terminal.

Step 1: Initialize the Vector Database
On the Vector Search Engine tab, click "Store All Letters in VectorDB"
Watch the progress bar as it simulates the ingestion pipeline
Note the statistics: 5 letters processed, number of chunks generated, 384 vector dimensions
Step 2: Run Semantic Queries
Try these queries and observe how semantic search finds relevant results:

"What are Warren Buffett's thoughts on the impact of COVID-19?"
"How does Berkshire approach stock repurchases and buybacks?"
"What makes a business a 'good' or 'wonderful' business to own?"
"What does Charlie Munger say about long-term investing?"
Try your own questions too! Notice how it finds relevant answers even when your words don't exactly match the letter text.

Step 3: Browse the Original Documents
Switch to the "Document Reference" tab
Select different shareholder letters from the dropdown
Compare the original PDF text with the search results you got

---

## Demo Complete!

What You Explored
LanceDB - An embedded vector database that requires zero infrastructure
Sentence Transformers - all-MiniLM-L6-v2 model generating 384-dim embeddings
Text Chunking - Splitting documents into overlapping chunks for better retrieval
Semantic Search - Finding relevant content by meaning, not keywords
Streamlit - Building interactive data apps with Python
Key Takeaways
Vector databases store meaning as numerical vectors, enabling similarity search
LanceDB's auto-embedding feature makes it easy - just pass raw text and it handles the rest
Chunking with overlap ensures context is preserved across document segments
Semantic search finds answers even when the query words don't match the document words
