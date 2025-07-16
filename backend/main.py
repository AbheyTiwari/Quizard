from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text
from embeddings import VectorStore
from llm import ask_gemini

app = FastAPI()
vector_store = VectorStore()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    text = extract_text(file)
    vector_store.add_text(text)
    return {"message": "File processed successfully"}

@app.get("/ask/")
async def ask_question(query: str):
    chunks = vector_store.search(query)
    context = "\n\n".join(chunks)
    prompt = f"Answer based on the following content:\n{context}\n\nQuestion: {query}"
    answer = ask_gemini(prompt)
    return {"answer": answer}
