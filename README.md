# 🤖 Gemini PDF Chatbot

A simple web app that lets you **upload a PDF** and **chat with it** using **Google Gemini (via LangChain)**.

Built using:
- 🧠 Gemini 2.0 Flash via LangChain
- ⚙️ Flask backend
- 🌐 React frontend
- 📄 PDF parsing + embedding with FAISS

---

## 📁 Project Structure



RAG/
│
├── backend/ # Flask backend
│ ├── app.py # Main app with /upload_pdf and /chat routes
│ ├── chat_handler.py # LangChain Gemini chat logic
│ ├── pdf_utils.py # PDF parsing + FAISS embedding
│ ├── requirements.txt # Python dependencies
│ └── .env # Google API key
│
├── frontend/ # React frontend (single page)
│ ├── src/
│ │ ├── App.js
│ │ └── App.css
│ ├── public/
│ └── package.json
│
└── README.md




---

## 🔧 Backend Setup (Flask)

### 1. Navigate to backend folder

```bash
cd backend


python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows


pip install -r requirements.txt


GOOGLE_API_KEY=your_google_gemini_api_key_here


python app.py


Frontend Setup (React)


1. Create React app inside frontend/


bash
npx create-react-app frontend


2. Replace contents


Replace frontend/src/App.js with your chatbot logic

Replace frontend/src/App.css with the styles provided


📌 (Use the React code provided in App.js and App.css in this project)

3. Start the frontend
bash
cd frontend
npm install
npm start



Runs on: http://localhost:3000

🚀 How to Use
Go to the frontend: http://localhost:3000

Upload a PDF

Ask any question related to that PDF

Get answers powered by Gemini + LangChain 🧠

🔓 CORS
CORS is fully enabled on the backend using:



python

from flask_cors import CORS
CORS(app)  # Allows all origins
🧠 Built With
LangChain

Flask

React

Google Gemini API

FAISS

