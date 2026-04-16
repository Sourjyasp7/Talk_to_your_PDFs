import streamlit as st
from ingest import process_pdf_to_store
from engine import get_answer_from_engine
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Dynamic RAG", layout="wide")
st.title("🤖 Dynamic Modular RAG")

# --- Session State Management ---
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "last_uploaded_file_id" not in st.session_state:
    st.session_state.last_uploaded_file_id = None

# --- PDF Upload ---
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Unique ID based on name and size to detect if a NEW file is uploaded
    file_id = f"{uploaded_file.name}_{uploaded_file.size}"

    # If the file is different from the last one, re-run ingest
    if st.session_state.last_uploaded_file_id != file_id:
        with st.spinner("🔄 File change detected. Re-indexing..."):
            # Call Ingest
            st.session_state.vector_store = process_pdf_to_store(uploaded_file)
            st.session_state.last_uploaded_file_id = file_id
            st.success("New index created!")

# --- Chat Interface ---
if st.session_state.vector_store:
    user_query = st.chat_input("Ask about this PDF...")
    
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Searching..."):
                # Call Engine
                response = get_answer_from_engine(user_query, st.session_state.vector_store)
                st.write(response["result"])
                
                with st.expander("Source Context"):
                    for doc in response["source_documents"]:
                        st.caption(doc.page_content[:250] + "...")
else:
    st.info("Upload a PDF to begin.")