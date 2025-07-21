import os
import tempfile
import asyncio
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv


def load_pdf_embeddings(file):
    # ✅ Patch: Create event loop for this thread if not already present
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # ✅ Save uploaded PDF to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        file.save(tmp_file.name)
        loader = PyPDFLoader(tmp_file.name)
        documents = loader.load()

    # ✅ Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # ✅ Check for empty content
    if not docs:
        raise ValueError("No valid text found in the uploaded PDF.")

    # ✅ Load Gemini embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key="api"  # Ensure this is in your .env
    )

    # ✅ Generate vectorstore
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
