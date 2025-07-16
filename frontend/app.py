import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="📄 Chat with Your Docs", layout="centered")
st.title("📄 Chat with Your Documents")
st.markdown("Upload a document and ask questions about its contents using Gemini AI.")

# Upload file
uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "xlsx", "txt"])
if uploaded_file:
    with st.spinner("Uploading and processing..."):
        response = requests.post(
            f"{API_URL}/upload/",
            files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        )
        if response.status_code == 200:
            st.success("✅ Document processed successfully!")
        else:
            st.error("❌ Failed to upload file.")

# Chat interface
query = st.text_input("Ask a question about the document")
if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        res = requests.get(f"{API_URL}/ask/", params={"query": query})
        if res.status_code == 200:
            st.write("🧠 Answer:", res.json()["answer"])
        else:
            st.error("❌ Failed to get an answer.")
