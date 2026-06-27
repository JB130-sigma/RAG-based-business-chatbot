from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
import shutil

# Load knowledge base
loader = TextLoader("data/company_faqs.txt")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Delete old vector database
if os.path.exists("vectorstore"):
    shutil.rmtree("vectorstore")

# Create new vector database
db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="vectorstore"
)

print("✅ Vector Database Created Successfully")
