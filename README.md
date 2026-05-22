# 🧠 RAG-CHATBOT

### *Where Documents Start Talking.*

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20By-LangChain-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/LLM-Groq-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Database-ChromaDB-purple?style=for-the-badge">
</p>

---

# 🌌 What is This?

Imagine uploading a PDF...

…and instead of manually searching through hundreds of lines,
the document itself becomes intelligent.

✨ Ask questions.
✨ Retrieve accurate answers.
✨ Chat naturally with your files.

This project is a **Retrieval-Augmented Generation (RAG) AI Chatbot** built using modern AI engineering tools that combines:

* ⚡ Ultra-fast LLM inference
* 🧠 Semantic search
* 📚 Vector databases
* 💬 Conversational memory
* 📄 Multi-document understanding

into one beautiful AI system.

---

# 🎥 Live Experience

### 🧑 User uploads a document

⬇

### 🔍 AI converts text into embeddings

⬇

### 🧠 ChromaDB stores semantic vectors

⬇

### 💬 User asks questions naturally

⬇

### 🚀 Groq-powered LLM generates grounded responses

---

# ✨ Features

## 📄 Intelligent Document Upload

Supports:

* PDF
* DOCX

The system automatically:

* extracts text
* chunks content
* generates embeddings
* stores semantic vectors

---

## 🧠 Conversational AI Memory

The chatbot remembers:

* previous questions
* previous answers
* session conversations

making the interaction feel human-like.

---

## ⚡ Groq-Powered Speed

Integrated with:

* **Llama 3.3 70B**
* **Groq Inference Engine**

for blazing-fast AI responses.

---

## 🔍 Semantic Retrieval

Instead of keyword matching,
the chatbot understands:

* meaning
* intent
* context

using vector embeddings.

---

## 🎨 Modern UI

Minimalistic and elegant Streamlit interface with:

* sidebar uploads
* live chatting
* clean layout
* responsive design
* document management

---

# 🏗️ Tech Stack

| Technology  | Purpose          |
| ----------- | ---------------- |
| Python      | Core Language    |
| FastAPI     | Backend API      |
| Streamlit   | Frontend         |
| LangChain   | AI Orchestration |
| ChromaDB    | Vector Storage   |
| HuggingFace | Embeddings       |
| Groq        | LLM Inference    |
| SQLite      | Chat History     |
| PyMuPDF     | PDF Processing   |

---

# 🧠 System Architecture

```text id="ahm7x0"
User Uploads Document
          ↓
Document Loader
          ↓
Chunking & Splitting
          ↓
Embedding Generation
          ↓
Chroma Vector Database
          ↓
Retriever
          ↓
LangChain RAG Pipeline
          ↓
Groq LLM
          ↓
AI Response
```

---

# 📂 Project Structure

```bash id="sdhrlu"
RAG-CHATBOT/
│
├── backend/
│   ├── backend.py
│   ├── nixpacks.toml
│   └── Procfile
│
├── frontend/
│   ├── frontend.py
│   └── requirements.txt
│
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash id="k18q8z"
git clone https://github.com/YOUR_USERNAME/RAG-CHATBOT.git
cd RAG-CHATBOT
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash id="0v0goj"
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash id="rx7pka"
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

### Backend

```bash id="85bn0h"
cd backend
pip install -r requirements.txt
```

### Frontend

```bash id="6i7r0h"
cd ../frontend
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env id="13d7nw"
GROQ_API_KEY=your_api_key
LANGSMITH_API_KEY=your_api_key
LANGCHAIN_TRACING_V2=true
```

⚠️ Never upload `.env` to GitHub.

---

# 🚀 Run Backend

```bash id="dn3ok1"
cd backend
uvicorn backend:app --reload
```

Backend runs at:

```text id="fvb5mr"
http://127.0.0.1:8000
```

---

# 🎨 Run Frontend

```bash id="v22snn"
cd frontend
streamlit run frontend.py
```

---

# ☁️ Free Deployment

| Service    | Platform        |
| ---------- | --------------- |
| Backend    | Render          |
| Frontend   | Streamlit Cloud |
| Repository | GitHub          |

---

# 🔥 API Endpoints

## 🏠 Home

```http id="6n0plu"
GET /
```

---

## 📄 Upload Documents

```http id="tqvzb0"
POST /upload
```

---

## 💬 Chat With AI

```http id="n6nnk8"
POST /chat
```

---

## 🆕 Create Session

```http id="hhx3cc"
GET /new-session
```

---

# 🧩 Core AI Concepts Used

## 🔹 Retrieval-Augmented Generation (RAG)

RAG allows AI to:

* retrieve real document context
* reduce hallucinations
* generate grounded answers

instead of relying only on pretrained memory.

---

## 🔹 Embeddings

Documents are transformed into:

* high-dimensional semantic vectors

allowing intelligent similarity search.

---

## 🔹 Vector Database

ChromaDB stores embeddings and retrieves the most relevant chunks during conversations.

---

# 🌟 Future Enhancements

* 🌙 Dark Mode
* 🔐 Authentication
* 🗣️ Voice Assistant
* 📊 Analytics Dashboard
* ☁️ Cloud Storage
* 🧠 Multi-Vector Retrieval
* 🐳 Docker Support
* 📱 Mobile Responsive UI

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push code
5. Open Pull Request

---

# 👨‍💻 Author

## Abhishek Choudhary

🚀 AI Engineer
🧠 LangChain Developer
⚡ Full Stack Builder

---

# ⭐ Show Support

If this project helped you:

🌟 Star the repository
🍴 Fork the project
📢 Share with developers

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00F7FF&center=true&vCenter=true&lines=AI+that+understands+documents.;Chat+with+your+data.;Built+with+LangChain+%26+Groq.;Future+of+RAG+starts+here.">
</p>

<p align="center">
  <b>“The future of document intelligence is conversational.”</b>
</p>

