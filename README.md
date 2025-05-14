# Resume Screening App

This project uses machine learning to screen resumes for job applications. It matches resumes against job descriptions to determine the most relevant applicants. This project is built using BERT embeddings for accurate predictions.

## Requirements

Before you start, ensure you have the following installed:
* Python 3.7+
* pip (Python package manager)

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/jahanvimalviya/resume_screening_app.git
    cd resume_screening_app
    ```

2. **Create a Virtual Environment:**
    For **Windows**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    For **Mac/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## Features

* **Resume Matching**: Matches resumes with job descriptions based on skills, experience, and more.
* **Model**: Trained using BERT embeddings for high accuracy.

## Notes

* The **model files** are pre-trained and stored in the repository. Please do not add personal data or resumes to the repo.
* Make sure that the environment setup is done properly to avoid errors when running the application.
* To test locally, ensure you have the `resume_match_model.pkl` and `label_encoder.pkl` files available.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

* BERT embeddings for natural language processing.
* Streamlit for easy web app development.
