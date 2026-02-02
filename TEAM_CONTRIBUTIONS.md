# Team Contributions

## Team Members

1.  **Yijia Kang** - Student ID: 33344554
2.  **Manasvi Vardham** - Student ID: 53548175
3.  **Akansha Rawat** - Student ID: 63153551

------------------------------------------------------------------------

## Project Roles Overview

-   **Development Phase:** Led by **Yijia Kang**, focusing on the codebase, algorithms, and AI model integration.
-   **Testing & QA Phase:** Led by **[Teammate 1 Name]** and **Akansha Rawat**, focusing on system stability and result verification.
-   **Demonstration Phase:** Led by **Akansha Rawat** (Video Production) and **[Teammate 2 Name]** (Scenario Design).

------------------------------------------------------------------------

## Detailed Task Breakdown

### Member 1: Yijia Kang

-   **System Architecture:** Designed the end-to-end RAG (Retrieval-Augmented Generation) pipeline.
-   **Implementation:** Wrote the core Python scripts:
    -   `data_prep.py` for data cleaning.
    -   `main.py` for the CLI engine and search logic.
    -   `app.py` for the Streamlit web interface.
-   **AI Integration:** Implemented `Sentence-BERT` for vector embeddings and `Flan-T5` for the Q&A generation.

### Member 2: Manasvi Vardham

-   **Demo Video Production:** Responsible for recording the screen capture of the software in action, editing the footage, and producing the final 2-3 minute submission video.
-   **Functional Testing:** Conducted "Black Box Testing" on the Web Interface (`app.py`) to ensure all buttons and search features work without crashing.
-   **Performance Check:** Verified that the "Similarity Score" feature displays correctly for various queries.

### Member 3: Akansha Rawat

-   **Resolved critical system compatibility issues:** Debugged and fixed Unicode encoding errors (cp1252 codec) and implemented regex-based filename sanitization to handle invalid Windows filesystem characters (\", :, /, *, ?, <>, |), preventing file I/O failures during document generation
-   **Optimized LLM integration and RAG pipeline:** Fixed empty output generation by tuning hyperparameters (max_length=200, min_length=15, num_beams=5, no_repeat_ngram_size=3) and implemented fallback mechanism using extractive summarization when the model fails to generate responses
-   **Debugged memory allocation failures:** Resolved OSError (paging file too small) when loading flan-t5-base by downgrading to flan-t5-small and configuring PyTorch for CPU inference, ensuring the system runs on resource-constrained environments
-   **Developed production-ready Streamlit web interface:** Built app.py with session state management, model caching, dynamic top-K retrieval controls, and interactive UI components (example query buttons, expandable document previews)
-   **Validated end-to-end system integration:** Performed comprehensive testing across Jupyter Notebook, CLI, and Streamlit environments, ensuring robust error handling, data pipeline validation (CSV schema corrections), and cross-platform compatibility
