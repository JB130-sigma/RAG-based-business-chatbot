import time
import streamlit as st
from rag_bot_pipeline import ask_question

st.set_page_config(page_title="Enterprise RAG Bot")

st.title("🤖 Enterprise RAG Bot")

question = st.chat_input("Ask a question")

if question:

    st.chat_message("user").write(question)
    
    start = time.time()

    answer, docs = ask_question(question)

    end = time.time()
    
    st.caption(f"Response time: {end-start:.2f}s")

    st.chat_message("assistant").write(answer)

    with st.expander("📄 View Retrieved Context"):

        for i, doc in enumerate(docs, start=1):

            st.markdown(f"**Chunk {i}:**")

            st.write(doc.page_content)
            
            st.write(f"**Source:** {doc.metadata['source']}")

            st.divider()



