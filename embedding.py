import os
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pathlib import Path

model = SentenceTransformer("all-MiniLM-L6-v2")

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

