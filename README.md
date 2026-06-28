# 🤖 Enterprise RAG Bot

A Retrieval-Augmented Generation (RAG) chatbot that answers business-related questions using a company knowledge base instead of relying on the Large Language Model's internal knowledge.

The application uses semantic search with vector embeddings to retrieve relevant information from enterprise documents and generates accurate responses using a locally hosted Llama 3 model through Ollama.

# 📌 Features

* 📄 Enterprise knowledge base using text documents
* 🔍 Semantic search with vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 💾 ChromaDB vector database
* 🤖 Local Llama 3 inference using Ollama
* 💬 Interactive Streamlit chat interface
* 📚 Retrieved context viewer for transparency
* 🔒 Reduced hallucination by grounding answers in retrieved documents


# 🏗️ Project Architecture

```
                 User Question
                       │
                       ▼
              Streamlit Interface
                       │
                       ▼
             HuggingFace Embeddings
                       │
                       ▼
              Chroma Vector Database
                       │
             Top-K Relevant Chunks
                       │
                       ▼
            Prompt Construction (RAG)
                       │
                       ▼
               Llama 3 (Ollama)
                       │
                       ▼
              Generated Response
```

---

# ⚙️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Llama 3 (Ollama)

### Framework

* LangChain

### Vector Database

* ChromaDB

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

---

# 📂 Project Structure

```
enterprise-rag-bot/

│── app.py
│── rag_bot_pipeline.py
│── create_vector_db.py
│── requirements.txt
│── README.md
│
├── data/
│     └── company_faqs.txt
│
├── vectorstore/
│
└── screenshots/
```


# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/enterprise-rag-bot.git

cd enterprise-rag-bot
```


## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama.

Pull Llama 3 model

```bash
ollama pull llama3
```

Verify installation

```bash
ollama list
```

---

## Build Vector Database

```bash
python create_vector_db.py
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📖 How It Works

### Step 1

The company knowledge base is loaded.

↓

### Step 2

Documents are split into smaller chunks.

↓

### Step 3

Each chunk is converted into vector embeddings.

↓

### Step 4

Embeddings are stored inside ChromaDB.

↓

### Step 5

When the user asks a question, semantic search retrieves the most relevant chunks.

↓

### Step 6

The retrieved context is injected into the Llama 3 prompt.

↓

### Step 7

The LLM generates an answer grounded in the retrieved context.

---

# 📷 Screenshots

## Chat Interface

(Add Screenshot Here)

---

## Retrieved Context

(Add Screenshot Here)

---

# 🧪 Example Questions

### Pricing

* What does the CRM Starter Plan cost?
* What is the Enterprise Plan price?

### Plans

* What features are included in the Enterprise Plan?
* How many users does the Professional Plan support?

### Support

* Is WhatsApp support available?
* Does Enterprise include dedicated account management?

### Invalid Questions

* Who is the CEO?
* What is the company's stock price?
* Where is the headquarters?

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Prompt Engineering
* Local LLM Deployment
* Streamlit Application Development
* LangChain Pipelines

---

# 🔮 Future Improvements

* PDF document support
* Multiple document ingestion
* Chat history
* Source citations with page numbers
* Response streaming
* Docker deployment
* FastAPI backend
* Authentication
* Production logging

---

# 👨‍💻 Author

**Jeet Bhandari**

AI & Machine Learning Enthusiast

