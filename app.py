import streamlit as st
from rag_bot_pipeline import ask_question

st.title("Enterprise RAG Bot")

question = st.chat_input(
    "Ask a question"
)

if question:

    st.chat_message("user").write(question)

    answer = ask_question(question)

    st.chat_message("assistant").write(answer)
def calculate_confidence(docs):
    return round(len(docs) / 5, 2)

    result = {
    "answer": answer,
    "sources": [d.page_content for d in docs],
    "confidence": round(calculate_confidence(docs), 2)
    }
    st.write(f"Confidence Score: {result['confidence']}")