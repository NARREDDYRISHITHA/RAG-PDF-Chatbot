# RAG-PDF-Chatbot
# 📄 RAG PDF Chatbot using Gemini & Streamlit

This project is a **PDF Question-Answering Chatbot** powered by **Retrieval-Augmented Generation (RAG)**, **FAISS**, **HuggingFace Embeddings**, and **Google Gemini API**. Upload any PDF and ask natural-language questions — the bot retrieves relevant sections from the PDF and gives you intelligent, contextual answers.

![demo](<img width="1250" height="859" alt="image" src="https://github.com/user-attachments/assets/0ee9279f-96d5-4164-8112-19e745f081f0" />
) <!-- (Optional: Add demo GIF or screenshot) -->

---

## 🚀 Features

- ✅ Upload and read any PDF file
- 🔍 Automatically extracts and chunks the text
- 🧠 Builds a vector index using HuggingFace embeddings & FAISS
- 🤖 Uses Google Gemini (Generative AI) to generate context-aware answers
- ⚡ Built with Streamlit for an interactive UI

---

## 🧰 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)
- **Embeddings**: [HuggingFace MiniLM](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **LLM**: [Google Gemini API](https://ai.google.dev/)
- **PDF Parsing**: `PyPDF2`

---

## 📁 Folder Structure
rag_pdf_chatbot/
├── main.py # Streamlit frontend app
├── rag_utils.py # All backend logic (RAG flow)
├── .env # Gemini API key
├── requirements.txt # Python dependencies
└── README.md


---

## 🛠️ Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag_pdf_chatbot
