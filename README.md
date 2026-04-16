# 🤖 Modular PDF-RAG Assistant

A professional-grade **Retrieval-Augmented Generation (RAG)** application built with **LangChain**, **OpenAI**, and **Streamlit**. This project enables users to upload PDF documents and engage in context-aware conversations, grounding AI responses in the provided data to minimize hallucinations.

---

## 🌟 Key Features
- **Modular Architecture:** Clean separation between Data Ingestion, Retrieval Engine, and UI.
- **Dynamic Re-indexing:** Detects file changes and updates the vector store automatically using session states.
- **Stateful Processing:** Caches embeddings in memory to optimize for cost, speed, and API efficiency.
- **Explainable AI:** Displays the exact document snippets used to generate every answer.

---

## 🏗️ Project Architecture



The project is split into three core modules:
1.  **`ingest.py`**: The Ingestion pipeline. Handles PDF loading, text chunking, and vectorization.
2.  **`engine.py`**: The Retrieval Logic. Manages the semantic search and connection to OpenAI.
3.  **`app.py`**: The Orchestrator. A Streamlit interface that manages user interactions and session memory.

---

## 🛠️ Project Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-rag-project.git](https://github.com/your-username/your-rag-project.git)
cd your-rag-project