
<h1 align="center">✨ Quizard: Your AI PDF Sidekick ✨</h1>

> _“Because scrolling through 92 pages just to answer **"Who was the chief guest?"** is so 2010...”_

---

### 📖 What is Quizard?

**Quizard** is a fast, flashy, full-stack AI-powered tool that reads your PDF documents and answers questions in seconds using **Google Gemini**!  
Whether you're prepping for a presentation, digging through long reports, or impressing your boss — **Quizard's got your back**.

🧠 Powered by:
- 🔥 FastAPI + Streamlit
- 🤖 Google Gemini (Generative AI)
- 📄 PDF extraction via PyMuPDF
- ⚡ Real-time Q&A like magic

---

### 🎯 Features

✅ Upload any PDF  
✅ Ask questions like “What is this doc about?” or “How many participants?”  
✅ Get AI-generated answers  
✅ See logs & results instantly  
✅ Easy to host, even easier to flex 💁‍♂️

---

### ⚙️ Setup Guide

#### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/quizard.git
cd quizard
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

 Add Your Gemini API Key
```
GOOGLE_API_KEY=your-gemini-api-key-here
```
Run Backend
```
cd backend
uvicorn main:app --reload
```
Run Frontend (in new terminal)
```
cd frontend
streamlit run app.py
```
<h2>Example Usage</h2>
Upload your PDF, ask:

👤 Who is this addressed to?
🎤 Who is the speaker?
🏆 What’s the framework?
📍 How many unauthorized settlements are there?
It. Just. Answers. 💥

🚀 Tech Stack
Layer	Tech
🧠 LLM	Google Gemini Pro
📦 Backend	FastAPI + Uvicorn
🎨 Frontend	Streamlit
📄 PDF	PyMuPDF (fitz)
🌐 API	REST

🧙 Future Plans
🔍 OCR for scanned PDFs

📊 PDF summaries & dashboards

🌍 Multi-language support

📱 Mobile UI with Flutter/React Native

🧵 Thread memory using vector DBs
