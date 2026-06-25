from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

retriever = db.as_retriever(
    search_kwargs={"k":3}
)

llm = Ollama(model="llama3")


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer only using the context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response