import os
import fitz
import io
from docx import Document
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract full text from uploaded PDF"""
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = Document(io.BytesIO(file_bytes))
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return text