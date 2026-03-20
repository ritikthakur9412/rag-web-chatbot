import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from utils.web_loader import load_web_data
from utils.vectorstore import create_vectorstore

# 🔹 Title
st.title("🌐 Web RAG Chatbot with Memory")

# 🔹 Input URL
url = st.text_input("Enter Website URL")

# 🔹 Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None

if "store" not in st.session_state:
    st.session_state.store = {}

# 🔹 Load Website Button
if st.button("Load Website"):
    if url:
        docs = load_web_data(url)
        retriever = create_vectorstore(docs)

        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Answer only from context."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        # 🔹 Format docs
        def format_docs(docs):
            return "\n\n".join([d.page_content for d in docs])

        # 🔹 Chain (FIXED)
        chain = (
            {
                "context": lambda x: format_docs(retriever.invoke(x["input"])),
                "input": lambda x: x["input"],
                "history": lambda x: x["history"]
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        # 🔹 Memory function
        def get_session_history(session_id):
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = InMemoryChatMessageHistory()
            return st.session_state.store[session_id]

        # 🔹 Save chatbot
        st.session_state.chatbot = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history"
        )

        st.success("Website loaded successfully!")

# 🔹 Chat Input
if st.session_state.chatbot:
    user_input = st.chat_input("Ask something...")

    if user_input:
        response = st.session_state.chatbot.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": "user1"}}
        )

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

# 🔹 Display Chat
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)