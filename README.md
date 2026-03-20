# 🌐 Web RAG Chatbot with Memory (LangChain + Groq + Chroma)

## 🚀 Overview

This project is a **Conversational RAG (Retrieval-Augmented Generation) Chatbot** that allows users to chat with any website.

It extracts content from a given URL, stores it in a vector database, and uses a Large Language Model (LLM) to generate context-aware answers with conversation memory.

---

## ✨ Features

* 🌐 Chat with any website (URL-based input)
* 🧠 Conversation memory (context-aware responses)
* ⚡ Fast LLM responses using Groq API
* 🔍 Semantic search using Chroma Vector DB
* 💬 ChatGPT-like UI using Streamlit

---

## 🛠️ Tech Stack

* **LangChain (LCEL)** – Orchestration framework
* **Groq API** – LLM (Mixtral / LLaMA models)
* **ChromaDB** – Vector database
* **HuggingFace Embeddings** – Text embeddings
* **Streamlit** – Web UI
* **BeautifulSoup** – Web scraping

---

## 🧠 Architecture

User Input → Web Loader → Text Splitter → Embeddings → Chroma DB
→ Retriever → Prompt Template + Memory → Groq LLM → Response

---

## 📁 Project Structure

```
rag-web-chatbot/
│
├── streamlit_app.py      # Main Streamlit UI
├── requirements.txt
├── .env
│
├── utils/
│   ├── __init__.py
│   ├── web_loader.py     # Loads and splits web data
│   └── vectorstore.py    # Creates Chroma vector DB
│
└── chroma_db/            # Auto-generated vector database
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/rag-web-chatbot.git
cd rag-web-chatbot
```

---

### 2️⃣ Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the app

```
python -m streamlit run streamlit_app.py
```

---

## 💬 Usage

1. Enter a website URL
2. Click **Load Website**
3. Start asking questions
4. Chatbot responds using website content + memory

---

## 📌 Example Use Cases

* Website Q&A chatbot
* Blog summarizer
* Knowledge assistant
* Research assistant

---

## 🎯 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings & Similarity Search
* Prompt Engineering
* Chat Memory (Session-based)
* LCEL (LangChain Expression Language)

---

## 🚀 Future Improvements

* Multi-URL support
* PDF + Web combined chatbot
* Authentication system
* Deployment (Render / HuggingFace)
* Better UI/UX

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* Groq
* HuggingFace
* Streamlit

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
