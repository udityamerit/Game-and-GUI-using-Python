import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import PyPDF2
import docx

# Load models (you can load fine-tuned model from local or Hugging Face)
@st.cache_resource
def load_models():
    bert_model = pipeline("question-answering", model="bert-base-uncased")
    roberta_model = pipeline("question-answering", model="deepset/roberta-base-squad2")
    fine_tuned_model = pipeline("question-answering", model="./fine-tuned-qa-model")  # Replace with path if fine-tuned locally
    embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # For answer re-ranking
    return bert_model, roberta_model, fine_tuned_model, embedder

# Load all models at startup
bert_model, roberta_model, fine_tuned_model, embedder = load_models()

# Extract text from uploaded files
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

# Ensemble Learning: Get answers from different models
def ensemble_answer(question, context):
    # Get answers from multiple models
    bert_answer = bert_model(question=question, context=context)
    roberta_answer = roberta_model(question=question, context=context)
    fine_tuned_answer = fine_tuned_model(question=question, context=context)
    
    # Combine answers
    answers = [bert_answer, roberta_answer, fine_tuned_answer]
    return rank_answers(question, answers)

# Re-ranking answers based on embeddings
def rank_answers(question, answers):
    question_embedding = embedder.encode(question)
    answer_embeddings = [embedder.encode(ans['answer']) for ans in answers]
    
    # Calculate cosine similarity
    similarities = [util.pytorch_cos_sim(question_embedding, ans_emb)[0] for ans_emb in answer_embeddings]
    
    # Re-rank based on similarity
    ranked_answers = sorted(zip(answers, similarities), key=lambda x: x[1], reverse=True)
    return ranked_answers[0][0]  # Return the best-ranked answer

# Post-processing to validate the answer
def validate_answer(document, answer):
    # Check how many times the answer appears in the document
    occurrences = document.lower().count(answer['answer'].lower())
    if occurrences > 1:
        answer['score'] += 0.1 * occurrences  # Boost confidence score if found multiple times
    return answer

# Streamlit app layout
st.title("Talk to Your Document")

# File uploader
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'pdf', 'docx'])

if uploaded_file is not None:
    # Extract the document content
    document_content = extract_text_from_file(uploaded_file)

    # Hide document content and notify the user
    st.success("Document uploaded successfully!")

    # Ask the question
    question = st.text_input("Ask a question about the document:")

    if st.button("Get Answer"):
        if question and document_content:
            # Use ensemble method to get the best answer
            with st.spinner("Processing... Please wait."):
                best_answer = ensemble_answer(question, document_content)

            # Validate answer based on occurrences in the document
            validated_answer = validate_answer(document_content, best_answer)

            # Display the answer
            st.subheader("Answer:")
            st.write(validated_answer['answer'])
            st.write(f"Confidence Score: {validated_answer['score']:.4f}")
        else:
            st.warning("Please enter a question.")

if __name__ == '__main__':
    st.write("Upload a document and ask your question.")
