import streamlit as st
from rag_utils import extract_text_from_pdf, create_vector_store, answer_query
import os

st.set_page_config(page_title="PDF Summarizer RAG")

st.title("📄 PDF Chatbot with RAG")
pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    with open(f"uploads/{pdf.name}", "wb") as f:
        f.write(pdf.read())

    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(f"uploads/{pdf.name}")
        vs = create_vector_store(text)
        st.success("PDF loaded and indexed!")

    query = st.text_input("Ask a question about this PDF:")

    if query:
        with st.spinner("Thinking..."):
            answer = answer_query(vs, query)
            st.write("🧠 Answer:", answer)
