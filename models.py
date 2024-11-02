from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_chat_model(gemini_key):
    google_api_key = gemini_key
    model_name = os.getenv("GOOGLE_GENAI_MODEL")
    temperature = os.getenv("MODEL_TEMPERATURE")

    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")

    return ChatGoogleGenerativeAI(
        google_api_key=google_api_key,
        model=model_name,
        temperature=temperature
    )
