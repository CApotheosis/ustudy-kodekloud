# Vector Database for GenAI

- Source: https://kodekloud.com/courses/vector-database-for-genai
- Fetched: 2026-09-05
- Status at fetch time: not yet released ("get a notification when course is released")

## Metadata

- Level: Beginner
- Modules: 7
- Topics: 74
- Video length: 04:48 hours (stated); actual sum of per-lesson timestamps below is close but not exact — treat the stated figure as authoritative
- Course includes: Certificate, Videos, Case Studies, Demos, Labs, Cloud Labs, Quizzes, Discord Community Support, Closed Captions, Story Format
- Categories: AI, DevOps
- Instructor: Raghunandana Krishnamurthy (Raghunandana Sanur) — Staff Data Engineer & MLOps Engineer at Talabat. Experience across GCP and AWS, big data platforms, DevOps/MLOps. Certifications: AWS Solutions Architect Associate, Cloudera Hadoop Admin, Airflow, Databricks Lakehouse. Tools: SageMaker, VertexAI, Prometheus, Grafana.
- Ratings/students: none shown

## Overview

Teaches how vector databases power modern AI applications by storing and retrieving data based on semantic similarity rather than exact queries. Covers embeddings, semantic search, RAG, recommendation systems, and cloud-based vector storage through hands-on labs.

## Requirements

- Basic knowledge of Python and AI/ML concepts recommended.

Target audience: AI/ML engineers building GenAI applications, data scientists working with embeddings/LLMs, software developers building intelligent applications, cloud engineers designing scalable AI systems, anyone interested in AI data architecture.

## Course Content

### Module 1: Introduction to Vector Databases and Generative AI (13 topics)
- Course Introduction — 04:13
- Vector Databases – The Definition — 01:47
- Demo: Ask Warren Anything You Want — 04:48
- Lab: Ask Warren Anything You Want
- Vectors, Made Simple — 04:48
- Demo: Visualization of Vectors in vectorDB — 06:04
- Lab: Visualization of Vectors in vectorDB
- Role of Vector Databases in GenAI — 02:26
- Airline Chatbot – Vector Database — 04:36
- Vector Databases vs Relational and NoSQL Databases — 03:18
- Demo: Setting up a Vector Database — 04:45
- Lab: Setting up a Vector Database
- How to Reach Out to KodeKloud and Engage with the Community

### Module 2: Vector Database Foundations (9 topics)
- What Does a Vector Database Store? — 03:56
- Vector Embeddings: Numerical Representations of Data — 03:42
- Querying Normal Database — 04:39
- Querying Vector Database — 04:00
- Demo: Difference in querying a normal DB vs vectorDB — 07:03
- Lab: Difference in querying a normal DB vs vectorDB
- Vector Querying Methods — 04:32
- When to Use Which Query Method? – Part 1 — 05:18
- When to Use Which Query Method? – Part 2 — 04:47

### Module 3: From Data to Vectors: The Embedding Layer (11 topics)
- From Data to Vectors: The Embedding Layer — 01:22
- Embedding Models — 03:56
- Text Embedding Models — 03:20
- Demo: Text Embedding with sentence transformer — 09:05
- Lab: Text Embedding with sentence transformer
- Image Embedding Models — 03:27
- Demo: Image Embedding — 06:06
- Lab: Image Embedding
- Audio Embedding Models — 03:58
- Video Embedding Models — 03:48
- Choosing and Optimizing Embedding Models — 04:58

### Module 4: Vector Similarity Explained (12 topics)
- Three Ways to Measure Similarity — 04:18
- Cosine Similarity — 04:46
- Euclidean Distance — 04:13
- Dot Product Similarity — 03:37
- Demo: Vector Search Metrics in 2D — 04:41
- Lab: Vector Search Metrics in 2D
- Comparing Cosine, Dot Product, and Euclidean Similarity — 04:04
- Fruit Embedding – Similarity Metrics in Action — 04:45
- How Similarity Results Can Differ — 06:45
- Demo: Setting up Vectors for Fruits — 04:13
- Demo: Query a New Fruit Across 3 Searches — 06:12
- Lab: Vector Similarity lab

### Module 5: Building Vector Storage on AWS S3 (8 topics)
- S3 Vector Buckets? — 05:02
- Demo: Creating an S3 Vector Bucket — 02:17
- Demo: Creating an IAM policy for S3 Vector Buckets — 02:50
- Key Features of S3 Vector Buckets — 05:50
- Demo: Accessing the S3 Vector Buckets — 03:56
- Demo: Embedding and Accessing Vectors from S3 Vector Buckets — 07:32
- S3 Vector Buckets vs Standard S3 Buckets — 06:14
- S3 Vector Buckets vs Vector Databases — 05:44

### Module 6: Vector Database Landscape (7 topics)
- Vector Database Landscape — 01:56
- Pinecone Vector Database — 02:42
- Weaviate Vector Database — 03:21
- Milvus Vector Database — 03:22
- Choosing Your Vector Database — 03:10
- Vector Database Feature Comparison — 03:36
- VectorDB Benchmark — 06:09

### Module 7: Vector Database Internals (14 topics)
- Vector Database Internals — 01:50
- Indexing in Vector Database — 03:22
- Demo: Understanding Indexing in Vector Database — 04:50
- HNSW Multi-Layered Graph Structure — 04:18
- HNSW Construction and Adoption — 04:06
- Quantization — 03:25
- Real-World Example of Quantization — 02:19
- Demo: Understand Binary Quantization — 05:12
- Lab: Understand Binary Quantization
- Index Maintenance — 02:26
- Strategy 1 – Write First, Index Later — 02:04
- Strategy 2 – Merge Small Pieces — 02:11
- Strategy 3 – Rebuild Sometimes — 02:57
- Applying Index Maintenance - Customer Care Chat Data — 04:13
