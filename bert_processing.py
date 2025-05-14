import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to generate BERT embeddings
def get_bert_embedding(text):
    """
    Generate BERT embeddings for a given text.
    """
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract [CLS] token embedding (first token)
    cls_embedding = outputs.last_hidden_state[0][0].numpy()
    
    return cls_embedding

# Function to calculate cosine similarity and combined embeddings
def calculate_match_score(resume, jd):
    """
    Calculate match score and combined embedding between resume and JD.
    """
    # Get embeddings
    resume_embedding = get_bert_embedding(resume)
    jd_embedding = get_bert_embedding(jd)

    # Calculate cosine similarity
    match_score = cosine_similarity([resume_embedding], [jd_embedding])[0][0]

    # Combine embeddings (optional step, can be used for further analysis)
    combined_embedding = np.concatenate((resume_embedding, jd_embedding))

    return match_score, combined_embedding

# Function to classify the match status
def classify_match(match_score):
    """
    Classify the match status based on the score.
    """
    if match_score >= 0.88:
        return "High Match"
    elif match_score >= 0.75:
        return "Partial Match"
    else:
        return "Low Match"
