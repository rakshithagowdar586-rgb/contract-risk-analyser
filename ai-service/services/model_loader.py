from sentence_transformers import SentenceTransformer

model = None

def load_model():
    global model
    if model is None:
        print("Loading sentence-transformers model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model