## Document Embedding Visualization with ChromaDB

What You'll Build
In this lab, you will complete a Jupyter notebook that builds a full document embedding pipeline — loading a PDF, chunking it, storing embeddings in ChromaDB, and visualizing the vector space in interactive 3D using Plotly.

Pipeline at a Glance
PDF Ingestion: Extract text from use_2025_budget.pdf using pypdf
Text Chunking: Split into 500-character chunks with 50-character overlap
Embeddings: Convert chunks to 384-dimensional vectors via all-MiniLM-L6-v2
Vector Storage: Persist embeddings in ChromaDB on disk
3D Visualization: Reduce 384-D to 3-D with PCA and plot with Plotly
You'll fill in 6 gaps in the student notebook, answer 3 concept questions, then explore the interactive visualization!

---

## Task 1: Access the Jupyter Notebook

Lab Environment Is Ready
The Jupyter Notebook container is already running with all dependencies pre-installed, including ChromaDB, sentence-transformers, pypdf, scikit-learn, and Plotly. Click the Jupyter Notebook button above to open it.

Step 1: Get the Jupyter Token
Run this command in the terminal to retrieve the access token:

docker logs embedding-viz 2>&1 | grep token
Step 2: Set a New Password
Click the Jupyter Notebook button above. On the login page, enter the token you copied into the Token field, then set a new password and click Log in and set new password. You can then use the password for future logins.

Step 3: Open the Student Notebook
Once logged in, open chroma_embedding_visualization_student.ipynb and proceed to the next tasks.

---

## 

---

## 

---

## 

---

## 

---

## 

---

## 

---

## 