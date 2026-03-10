import faiss
import numpy as np
import os

class VectorStore:
    def __init__(self, dim: int, index_path="vector.index", meta_path="metadata.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.load()

    def add(self, vectors: list, texts: list):
        np_vectors = np.array(vectors).astype("float32")
        self.index.add(np_vectors)
        self.metadata.extend(texts)
        self.save()

    