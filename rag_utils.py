import os
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Extract text from PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# 2. Split into chunks
def split_text(text, chunk_size=1000, chunk_overlap=200):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.create_documents([text])

# 3. Use HuggingFace embeddings instead of Google Embeddings
def create_vector_store(text):
    docs = split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

# 4. Use Gemini for answer generation
def answer_query(vectorstore, query):
    relevant_docs = vectorstore.similarity_search(query, k=4)
    context = "\n".join(doc.page_content for doc in relevant_docs)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
    prompt = f"""
    Use the context below to answer the user's question.

    Context:
    {context}

    Question:
    {query}

    Answer:"""
    
    response = model.generate_content(prompt)
    return response.text
