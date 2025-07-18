# 📄 RAG PDF Chatbot using Gemini & Streamlit

This project is a **PDF Question-Answering Chatbot** powered by **Retrieval-Augmented Generation (RAG)**, **FAISS**, **HuggingFace Embeddings**, and **Google Gemini API**. Upload any PDF and ask natural-language questions — the bot retrieves relevant sections from the PDF and gives you intelligent, contextual answers.


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
```
rag_pdf_chatbot/
├── main.py # Streamlit frontend app
├── rag_utils.py # All backend logic (RAG flow)
├── .env # Gemini API key
├── requirements.txt # Python dependencies
└── README.md

```


---
## 📷 ScreenShot

<img src="https://github.com/user-attachments/assets/3f8375a8-c8aa-402e-9b34-4a08a394dba9" alt="Screenshot" width="500"/>


## 🛠️ Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag_pdf_chatbot
```
### 2. Install Dependencies
 ```
pip install -r requirements.txt
```
### 3. Set Up Environment Variable
 ```
GEMINI_API_KEY=your_google_generative_ai_key_here
 ```

### 4. Run the App
```
python -m streamlit run main.py
```
