# Financial News Semantic Search Engine

## Overview

This project implements a **production-ready Semantic Search Engine** tailored for **financial news analysis**.\
Unlike traditional keyword-based search, this system leverages **vector embeddings** to understand the **semantic meaning** behind user queries. It integrates a **Retrieval-Augmented Generation (RAG)** pipeline that retrieves relevant financial news articles and uses a **Large Language Model (LLM)** to generate **context-aware natural language answers**.

The system supports both a **Command Line Interface (CLI)** and a **Streamlit Web Application**, providing flexible and user-friendly interaction.

------------------------------------------------------------------------

## Dataset & Domain

**Domain:** Financial News (Instructor-approved category: *News*)\
**Source File:** `dataset.csv`

### Dataset Statistics (Meets Course Requirement)

| Metric | Count |
|------------------------------------|------------------------------------|
| Raw Records | **1,839** |
| Final Cleaned Documents | **1,659** *(Exceeds minimum requirement of 100 documents)* |

------------------------------------------------------------------------

## Data Cleaning Process

-   **Deduplication:** Removed duplicate news articles based on content\
-   **Noise Filtering:** Removed empty rows, NaN values, and crawler artifacts (e.g., `"[]"`)\
-   **Normalization:** Cleaned text formatting and removed irrelevant metadata

Final output: **1,659 high-quality financial news documents**, each stored as an individual `.txt` file.

------------------------------------------------------------------------

## Key Features

### Semantic Search

-   Embedding model: **Sentence-BERT (`all-MiniLM-L6-v2`)**
-   Retrieves documents based on **semantic similarity**, not keyword overlap
-   Uses **Cosine Similarity** for ranking
-   Returns **Top-K most relevant results**

------------------------------------------------------------------------

### AI-Powered Question Answering (RAG)

-   LLM model: **Google Flan-T5 (`flan-t5-base`)**
-   Generates answers **grounded in retrieved financial news**
-   Reduces hallucination by restricting responses to retrieved context
-   Ensures responses are **fact-based and explainable**

------------------------------------------------------------------------

### Automated Data Pipeline

-   `data_prep.py` converts raw CSV into structured `.txt` document corpus\
-   Ensures reproducibility and clean corpus generation

------------------------------------------------------------------------

### Dual Interfaces

-   **CLI Interface** (`main.py`) — lightweight terminal-based search\
-   **Web Interface** (`app.py`) — interactive UI built with **Streamlit** *(Bonus)*

------------------------------------------------------------------------

## Project Structure

``` text
.
├── dataset.csv              # Original raw dataset
├── news_documents/          # Generated cleaned text corpus
├── data_prep.py             # Data cleaning & document generator
├── main.py                  # Command Line Interface (CLI)
├── app.py                   # Streamlit Web Application
├── requirements.txt         # Dependencies
├── README.md                # Project overview & usage
├── ARCHITECTURE.md          # Technical system design
├── TEAM_CONTRIBUTIONS.md    # Team roles & contributions
```

## Installation & Setup

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package manager)

### Step 1: Install Dependencies

Open your terminal or command prompt and run:

```         
pip install -r requirements.txt
```

### Step 2: Prepare the Data

Before running the search engine, you must generate the document corpus from the CSV file. Run the following command:

```         
python data_prep.py
```

*This will create a news_documents folder and populate it with individual text files.*

## Usage

### Option A: Run Command Line Interface (CLI)

Use this for a simple text-based interaction in your terminal.

```         
python main.py
```

-   **To exit:** Type `exit`, `quit`, or `q`.

### Option B: Run Web Interface (Streamlit)

Use this for a visual experience with better formatting.

```         
streamlit run app.py
```

-   This will automatically open the application in your default web browser (usually at <http://localhost:8501>).

## Technical Architecture

1.  **Data Ingestion:**
    -   Raw CSV data is split into individual `.txt` files to simulate a real-world document database.
2.  **Vector Embedding:**
    -   Model: `sentence-transformers/all-MiniLM-L6-v2`
    -   Documents and user queries are converted into high-dimensional vectors.
3.  **Retrieval:**
    -   Cosine Similarity is calculated to find the top 3 most relevant documents.
4.  **Generation (RAG):**
    -   Model: `google/flan-t5-base`
    -   The retrieved text is fed into the LLM as context to answer the user's question accurately.

## Example Queries

Try asking these questions to test the system:

-   "Who announced cash dividends?"
-   "What is the news about Alwasail Industrial?"
-   "What are the latest financial results for Bawan Co?"
