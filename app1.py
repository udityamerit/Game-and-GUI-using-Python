# app.py

import streamlit as st
from transformers import pipeline
import os
import PyPDF2
import docx

# Load the Question Answering model ONCE
@st.cache_resource
def load_qa_model():
    return pipeline("question-answering")

qa_pipeline = load_qa_model()

# Streamlit app layout
st.title("Talk to Your Document")

# File uploader
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'pdf', 'docx'])

def extract_text_from_file(file):
    """Extract text from uploaded file (txt, pdf, or docx)."""
    if file.type == 'text/plain':
        return file.read().decode('utf-8')
    elif file.type == 'application/pdf':
        reader = PyPDF2.PdfReader(file)
        return ''.join([page.extract_text() for page in reader.pages])
    elif file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    return None

def get_answer_from_document(document_content, question):
    """Extract relevant answer using QA model."""
    # Limit the document content to the first 500 words to speed up processing.
    if len(document_content.split()) > 500:
        document_content = ' '.join(document_content.split()[:500])
    
    return qa_pipeline({
        'context': document_content,
        'question': question
    })

if uploaded_file is not None:
    # Extract the document content
    document_content = extract_text_from_file(uploaded_file)

    # Hide the document content from the user
    st.success("Document uploaded successfully!")

    # Ask the question
    question = st.text_input("Ask a question about the document:")

    if st.button("Get Answer"):
        if question and document_content:
            # Use the QA model to find the answer
            with st.spinner("Processing... Please wait."):
                result = get_answer_from_document(document_content, question)

            # Display the answer
            st.subheader("Answer:")
            st.write(result['answer'])
            st.write(f"Confidence Score: {(result['score'])*100:.4f}")
        else:
            st.warning("Please enter a question.")
