from transformers import BertTokenizer, BertModel

# Test if the imports work
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

print("BERT Model and Tokenizer loaded successfully!")
