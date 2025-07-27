from faq import faq_chain, ingest_fag_data
import streamlit as st
# Load data first
ingest_fag_data()
# st.sidebar.button("Load FAQ Data", on_click=ingest_fag_data)
# 1. Title
st.title("FAQ Chatbot")

if "messages" not in st.session_state: 
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

input_paragraph = st.chat_input("Ask about NEFT, RTGS, Amortization, or any banking queries")

if input_paragraph:
    with st.chat_message("user"):
        st.markdown(input_paragraph)
    st.session_state.messages.append({'role': 'user', 'content': input_paragraph})

    response  = faq_chain(input_paragraph)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({'role': 'assistant', 'content': response})
    