import google.generativeai as genai
from backend.config import GEMINI_API_KEY

def load_model():
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

# Load the model once
gemini_model = load_model()
