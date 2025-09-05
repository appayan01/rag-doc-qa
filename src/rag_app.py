import streamlit as st

st.title("RAG Demo - Context Aware QA")
st.write("Upload a document and ask a question!")

uploaded_file = st.file_uploader("Upload a text file")
question = st.text_input("Enter your question:")

if uploaded_file and question:
    text = uploaded_file.read().decode("utf-8")
    st.write("📖 Retrieved text snippet:", text[:200])
    st.write("🤖 Answer (placeholder): This would normally come from a RAG pipeline.")
