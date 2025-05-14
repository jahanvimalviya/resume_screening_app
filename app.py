import streamlit as st
import joblib
from bert_processing import get_bert_embedding, calculate_match_score, classify_match
import pdfplumber
import os

# Define paths
MODEL_PATH = "D:/resume_screening_app/resume_match_model.pkl"
LABEL_ENCODER_PATH = "D:/resume_screening_app/label_encoder.pkl"

# Load the model and label encoder
if os.path.exists(MODEL_PATH) and os.path.exists(LABEL_ENCODER_PATH):
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
else:
    st.error("Model or label encoder not found. Please ensure the paths are correct.")
    st.stop()

st.title("Resume Screening and Job Matching")
st.write("Upload a resume (PDF or TXT) and a job description (PDF or TXT) to find the best match.")

# Function to read text from a TXT file with error handling
def read_txt(file):
    try:
        return file.read().decode('utf-8')
    except UnicodeDecodeError:
        file.seek(0)
        return file.read().decode('ISO-8859-1', errors='ignore')

# Function to read text from a PDF file
def read_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text

# File upload
uploaded_resume = st.file_uploader("Upload Resume (TXT or PDF)", type=["txt", "pdf"])
uploaded_jd = st.file_uploader("Upload Job Description (TXT or PDF)", type=["txt", "pdf"])

if uploaded_resume and uploaded_jd:
    # Read resume content
    if uploaded_resume.type == "text/plain":
        resume_text = read_txt(uploaded_resume)
    elif uploaded_resume.type == "application/pdf":
        resume_text = read_pdf(uploaded_resume)
    
    # Read JD content
    if uploaded_jd.type == "text/plain":
        jd_text = read_txt(uploaded_jd)
    elif uploaded_jd.type == "application/pdf":
        jd_text = read_pdf(uploaded_jd)

    # Display full resume and JD
    st.subheader("Uploaded Resume:")
    st.text_area("Resume Content", resume_text, height=300)

    st.subheader("Uploaded Job Description:")
    st.text_area("Job Description Content", jd_text, height=300)

    # Check if content is extracted
    if resume_text and jd_text:
        # Get BERT embeddings
        st.write("Generating BERT embeddings...")
        match_score, _ = calculate_match_score(resume_text, jd_text)

        # Get match status
        match_label = classify_match(match_score)

        # Display match score, percentage, and label
        match_percentage = round(match_score * 100, 2)
        st.subheader("Match Score:")
        st.write(f"Match Score: {match_score}")
        st.write(f"Match Percentage: {match_percentage}%")

        st.subheader("Match Result:")
        st.write(f"The resume is a **{match_label}** for the job description.")
    else:
        st.warning("Error extracting text from one or both files. Please check the files and try again.")
