# Resume Screening App

An AI-powered resume screening application that uses machine learning and BERT embeddings to match resumes with job descriptions. This application helps recruiters to efficiently screen resumes and determine the best matches for specific job roles.

---

## ✅ **Features:**
- Extracts text from resumes (PDF format).
- Embeds resume content using BERT for semantic understanding.
- Predicts job category based on resume content.
- Matches resumes against job descriptions to provide a similarity score.
- Displays match percentage and match/no match labels for easy interpretation.

## 📂 Project Structure:

/resume_screening_app/
│── app.py # Main Streamlit application
│── bert_processing.py # BERT embedding extraction logic
│── requirements.txt # List of required libraries
│── resume_match_model.pkl # Trained ML model for resume matching
│── label_encoder.pkl # Label encoder for job categories
│── .gitignore # Files/folders to ignore in Git
│── README.md # Project documentation

## 🚀 Installation Instructions

1. **Clone the Repository:**  
   Open a terminal and run:  
   ```bash
   git clone https://github.com/jahanvimalviya/resume_screening_app.git
   cd resume_screening_app

2)Create a Virtual Environment:
    python -m venv .venv

3)Activate the Virtual Environment:

    On Windows:
    .venv\Scripts\activate

On Mac/Linux:
    source .venv/bin/activate

4)Install Dependencies:
    pip install -r requirements.txt

5)Run the Application:
    streamlit run app.py

6)Deactivate the Environment (optional):
    deactivate


Install Dependencies
After creating and activating the virtual environment, install the required libraries using the following command:

pip install -r requirements.txt
This will install all the libraries listed in the requirements.txt file, including:
Streamlit

Transformers

Torch

Torchaudio

Torchvision

Pdfplumber

Scikit-Learn

Numpy


Model Files and Setup
The project requires two pre-trained model files:

resume_match_model.pkl - The trained model for resume matching.

label_encoder.pkl - The label encoder used during training.

