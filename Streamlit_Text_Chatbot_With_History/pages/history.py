import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory


# Retrieve the chat history
history = StreamlitChatMessageHistory(key="special_app_key")

# Display the chat history using Streamlit components
for msg in history.messages:
    if msg.type == "human":
        st.text(f"User: {msg.content}")
    elif msg.type == "ai":
        st.text(f"AI: {msg.content}")
