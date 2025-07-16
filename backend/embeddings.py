from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.chunks = []

    def add_text(self, text):
        chunks = text.split('\n\n')  # simple chunking
        vectors = model.encode(chunks)
        self.index.add(np.array(vectors).astype('float32'))
        self.chunks.extend(chunks)

    def search(self, query, k=3):
        query_vec = model.encode([query]).astype('float32')
        D, I = self.index.search(query_vec, k)
        return [self.chunks[i] for i in I[0]]
