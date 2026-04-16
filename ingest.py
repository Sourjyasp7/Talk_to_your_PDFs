import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import tempfile

def process_pdf_to_store(uploaded_file):
    # Create a temporary file to read the PDF
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # 1. Load and Split
    loader = PyPDFLoader(tmp_path)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(loader.load())

    # 2. Embed
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    
    # Cleanup temp file
    os.remove(tmp_path)
    
    return vectorstore