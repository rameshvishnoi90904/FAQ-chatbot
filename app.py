from faq import faq_chain, ingest_fag_data
import streamlit as st

st.sidebar.button("Load FAQ Data", on_click=ingest_fag_data)
# 1. Title
st.title("FAQ Chatbot")

# 2. Input box
input_paragraph = st.text_area("Enter a your query here")

# 3. Button
extract_button = st.button("Find Answer")

if extract_button:
    answer = faq_chain(input_paragraph)
    st.header("Results")
    st.write("Answer:", answer)