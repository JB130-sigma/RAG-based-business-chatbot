from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# -----------------------------
# Load embedding model
# -----------------------------
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load Vector Database
# -----------------------------
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

# -----------------------------
# Create Retriever
# -----------------------------
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

# -----------------------------
# Load Local LLM
# -----------------------------
llm = Ollama(model="llama3")


def ask_question(question):

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # If nothing retrieved
    if not docs:
        return "I could not find that information in the company knowledge base.", []

    # Build Context
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Debug (keep while learning)
    print("\n========== RETRIEVED CONTEXT ==========")
    print(context)
    print("=======================================\n")

    # Prompt
    prompt = f"""
You are an Enterprise CRM Assistant.

Rules:
1. Answer ONLY from the provided context.
2. Do NOT mention "according to the context."
3. Respond naturally and professionally.
4. Never use outside knowledge.
5. If the answer is not found, reply exactly:
I could not find that information in the company knowledge base.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate response
    answer = llm.invoke(prompt)

    return answer, docs
