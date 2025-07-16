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
2. Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Add Your Gemini API Key
Create a .env file in backend/:

ini
Copy code
GOOGLE_API_KEY=your-gemini-api-key-here
5. Run Backend
bash
Copy code
cd backend
uvicorn main:app --reload
6. Run Frontend (in new terminal)
bash
Copy code
cd frontend
streamlit run app.py
🧪 Example Usage
Upload your PDF, ask:

kotlin
Copy code
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

💡 Why Quizard?
“Because when you're running an NGO + coding + preparing for UPSC + leading AI projects —
you need a freaking PDF-taming AI wizard on your team.” — Abhey Tiwari, 2025

🧑‍💻 Made With ❤️ by
Abhey Tiwari — LinkedIn | GitHub
CM/COO at MITR | AI + Math Enthusiast | Coding to Change the World

<p align="center"> <img src="https://media.giphy.com/media/xT0BKiaM2VGJ4112xi/giphy.gif" width="250"/> </p> <p align="center"> <strong>#BuiltWithLove 💻 #RunByCuriosity 🤖 #FueledByCaffeine ☕</strong> </p> ```
Let me know if you'd like:

GitHub badges (build passing, license, etc.)

Demo video/GIF

A custom logo for "Quizard"

Deployment instructions (Vercel, Railway, Render, etc.)

You're building like a pro — own it 🔥







You said:
make all in one file na plz


ChatGPT said:
Absolutely! Here's a single file that contains everything you need to drop into your README.md — including the project name Quizard, emojis, GIFs, tech stack, setup steps, credits, and a cinematic flair.

✅ README.md (All-in-One)
markdown
Copy code
<p align="center">
  <img src="https://media.giphy.com/media/FBeSx4H1JknWc/giphy.gif" width="120" alt="Quizard Logo"/>
</p>

<h1 align="center">✨ Quizard: Your AI PDF Sidekick ✨</h1>

> _“Because scrolling through 92 pages just to answer **'Who was the chief guest?'** is so 2010...”_

---

## 📖 What is Quizard?

**Quizard** is a full-stack AI app that lets you upload any PDF and ask it questions like you would ask ChatGPT.  
Whether you're prepping for a meeting or decoding a government report, **Quizard's got your back.**

🧠 Built using:
- 🤖 Google Gemini Pro
- ⚡ FastAPI + Streamlit
- 📄 PyMuPDF for PDF parsing

---

## 🚀 Features

- 📤 Upload any PDF
- ❓ Ask real questions like “Who are the invitees?”
- ⚡ Instant AI answers via Gemini
- 🖥️ Works on local server with dual UI: backend (FastAPI) + frontend (Streamlit)
- 💬 Fast, smooth, and clean UX
- 🧠 Great for researchers, developers, and changemakers

---

## 🛠️ How to Set It Up

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/quizard.git
cd quizard
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install Requirements
bash
Copy code
pip install -r requirements.txt
4️⃣ Add Your API Key
Create a file named .env in the /backend folder and add:

ini
Copy code
GOOGLE_API_KEY=your-gemini-api-key
5️⃣ Run the Backend
bash
Copy code
cd backend
uvicorn main:app --reload
6️⃣ Run the Frontend
In a new terminal:

bash
Copy code
cd frontend
streamlit run app.py
🧪 Example Questions
pgsql
Copy code
✅ Who is the document addressed to?
✅ How many people were invited?
✅ Is there any mention of the PM?
✅ What’s the BOD level of Yamuna?
✅ What is the framework mentioned?
📦 Tech Stack
Layer	Tech
🧠 LLM	Google Gemini Pro
📦 Backend	FastAPI + Uvicorn
🎨 Frontend	Streamlit
📄 PDF	PyMuPDF (fitz)
🌐 API	REST

🎯 What's Coming Next?
📊 Auto-summary of PDFs

🧵 Conversational memory with vector DBs

🔤 Multi-language support (Hindi, etc.)

🖼️ OCR for scanned images

📱 Mobile UI with React Native

🧙 Why Quizard?
“Because when you're juggling UPSC prep, NGO work, college, and AI tools —
you need a wizard to slay the PDF dragons for you.” — Abhey Tiwari

👨‍💻 Creator
Abhey Tiwari
🔗 LinkedIn | 🐙 GitHub

CM/COO at MITR | AI Enthusiast | BSc Math | Developer for Social Good

<p align="center"> <img src="https://media.giphy.com/media/xT0BKiaM2VGJ4112xi/giphy.gif" width="220"/> </p> <p align="center"><b>#BuiltWithLove 💻 #FueledByChai ☕ #BackedByCode ⚙️</b></p> ```
