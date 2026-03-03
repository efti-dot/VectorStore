import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def uploading_screen():
    st.write("Upload Content!")
    uploaded_file = st.file_uploader(
        "Upload your document (PDF, DOCX, or image)", 
        type=["pdf", "docx"]
    )