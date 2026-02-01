# System Architecture

## High-Level Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system designed to analyze and query financial news. By combining semantic search with a generative language model, the system can retrieve specific news articles relevant to a user's question and generate a concise, natural language answer based on that content.

## Core Components

The architecture consists of four main processing layers:

### 1. Data Ingestion Layer (`data_prep.py`)

-   **Input:** A raw CSV dataset (`dataset.csv`) containing financial news articles.
-   **Processing:**
    -   The script iterates through the CSV rows.
    -   It cleans the text and combines the `title` and `content` columns to ensure context is preserved.
    -   **Output:** It generates individual `.txt` files in the `news_documents/` directory. This step simulates a real-world scenario where data is often unstructured and file-based.

### 2. Embedding & Indexing Engine

-   **Model Used:** `sentence-transformers/all-MiniLM-L6-v2`
-   **Function:**
    -   This model converts textual documents into **384-dimensional dense vectors** (embeddings).
    -   Unlike keyword search (BM25), these embeddings capture the *semantic meaning* of the text.
    -   **Storage:** For this implementation, embeddings are generated in-memory at runtime to ensure simplicity and portability.

### 3. Retrieval System (The "Search" Part)

-   **Metric:** **Cosine Similarity**.
-   **Workflow:**
    1.  The user's query (e.g., "Who announced dividends?") is encoded into a vector using the same embedding model.
    2.  The system calculates the cosine similarity between the query vector and every document vector in the corpus.
    3.  **Top-K Retrieval:** The system ranks the results and retrieves the top 3 documents with the highest similarity scores.

### 4. Generative AI Layer (The "Answer" Part)

-   **Model Used:** `google/flan-t5-base` (Sequence-to-Sequence LLM).

-   **Prompt Strategy:**

    -   The system constructs a prompt to guide the LLM. The format is structured as follows:

    ```         
    Question: <User Query>
    Context: <Content of Document 1> <Content of Document 2> ...
    Answer:
    ```

-   **Inference:** The LLM receives this prompt and generates an answer derived *strictly* from the provided context, minimizing hallucinations.

## Data Flow Pipeline

1.  **User Input:** User types a question in the CLI or Web Interface.
2.  **Vectorization:** The query is converted to a vector embedding.
3.  **Semantic Search:** The system finds the most relevant news snippets.
4.  **Context Construction:** Relevant snippets are concatenated into a single context block.
5.  **Generation:** The LLM reads the context and the question to synthesize an answer.
6.  **Presentation:** The system displays the AI answer, the source documents, and the similarity scores.

## Technology Stack

-   **Language:** Python 3.x
-   **Machine Learning Libraries:** PyTorch, Transformers (Hugging Face), Sentence-Transformers, Scikit-learn.
-   **User Interface:**
    -   **Streamlit:** For the web-based dashboard.
    -   **Standard I/O:** For the command-line interface.
-   **Data Handling:** Pandas, NumPy.
