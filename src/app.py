from dotenv import load_dotenv
import streamlit as st
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Felipe's GPT-3.5 Playground")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I'm Felipe's GPT-3.5 model. A powerful AI that can help you with a lot of things. How can I help you today?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state["messages"]
    )
    responseMessage = response["choices"][0]["message"]["content"]
    st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)


