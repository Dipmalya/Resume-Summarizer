# 🧠 Resume Summarizer using RAG (LangChain + Chroma)

## 📌 Overview

This project implements a simple **Retrieval-Augmented Generation (RAG)** pipeline to generate a **tailored professional summary of a resume** based on a given **Job Description (JD)**.

It leverages:

* **LangChain** for orchestration
* **Chroma DB** as a vector store
* **OpenAI LLMs** for summary generation
* **Python** for end-to-end implementation

The system extracts content from a resume PDF, retrieves the most relevant sections based on the job description, and generates a concise, targeted summary.

---

## 🚀 Features

* 📄 Load and process Resume PDF
* ✂️ Intelligent text chunking
* 🔍 Semantic search using embeddings
* 🧠 Context-aware summary generation
* 🎯 Tailored output aligned with job requirements
* 💾 Persistent vector database (Chroma)

---

## 🏗️ Architecture

```
Resume PDF → Text Chunking → Embeddings → Chroma Vector DB
                                             ↓
Job Description → Query → Retriever → LLM → Summary Output
```

---

## 📁 Project Structure

```
resume_rag/
│── main.py                # Entry point
│── config.py              # Configurations (API keys, paths)
│── resume_loader.py       # PDF loading & chunking
│── rag_pipeline.py        # Vector DB + RAG chain
│── prompts.py             # Prompt templates
│── requirements.txt       # Dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd Resume-Summarizer
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### Step 1: Index the Resume

Run once to create embeddings:

```python
build_index("data/sample_resume.pdf")
```

### Step 2: Generate Summary

Update the Job Description inside `main.py`:

```python
job_description = """Your job description here"""
```

Run the script:

```bash
python main.py
```
---

## 🧠 How It Works

1. **PDF Parsing** – Extracts text from resume
2. **Chunking** – Splits into manageable pieces
3. **Embedding** – Converts text into vectors
4. **Storage** – Saves vectors in Chroma DB
5. **Retrieval** – Finds relevant resume sections
6. **Generation** – LLM produces a tailored summary
