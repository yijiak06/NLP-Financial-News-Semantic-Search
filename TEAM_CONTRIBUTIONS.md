# Team Contributions

## Team Members

1.  **Yijia Kang** - Student ID: 33344554
2.  **Manasvi Vardham** - Student ID: 53548175
3.  **Akansha Rawat** - Student ID: 63153551

------------------------------------------------------------------------

## Project Roles Overview

-   **Development Phase:** Led by **Yijia Kang**, focusing on the codebase, algorithms, and AI model integration.
-   **Testing & QA Phase:** Led by **Manasvi Vardham** and **Akansha Rawat**, focusing on system stability and result verification.
-   **Demonstration Phase:** Led by **Akansha Rawat** and **Manasvi Vardham**.

------------------------------------------------------------------------

## Detailed Task Breakdown

### Member 1: Yijia Kang

-   **Data Engineering & Management:** Responsible for sourcing the raw financial news dataset, organizing the file structure, and executing comprehensive data cleaning (removing duplicates, filtering artifacts like `[]` and `nan`) to build a high-quality search corpus.
-   **System Architecture:** Designed the end-to-end RAG (Retrieval-Augmented Generation) pipeline.
-   **Implementation:** Wrote the core Python scripts:
    -   `data_prep.py` for automated data processing and regex-based filename sanitization.
    -   `main.py` for the CLI engine and search logic.
    -   `app.py` for the Streamlit web interface with session state management.
-   **AI Integration:** Implemented `Sentence-BERT` for vector embeddings and `Flan-T5` for Q&A generation.

### Member 2: Manasvi Vardham

-   **Demo Video Production:** Responsible for recording the screen capture of the software in action, editing the footage, and producing the final 2-3 minute submission video.
-   **Functional Testing:** Conducted "Black Box Testing" on the Web Interface (`app.py`) to ensure all buttons and search features work without crashing.
-   **Performance Check:** Verified that the "Similarity Score" feature displays correctly for various queries.

### Member 3: Akansha Rawat

-   **Environment Compatibility Testing:** Identified and tested the "paging file too small" memory issue on Windows environments, verifying the system's flexibility to switch between `flan-t5-base` and `flan-t5-small`.
-   **Cross-Platform Debugging:** Reported critical Windows-specific issues (e.g., Unicode encoding errors and invalid filename characters), which ensured the final code is robust across different operating systems.
-   **Integration Verification:** Validated that the `app.py` interface loads correctly and caches models as expected on local machines.
