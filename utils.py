import os
import fitz
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