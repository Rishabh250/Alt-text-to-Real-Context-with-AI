from models import get_chat_model

class AltTextGenerator:
    def __init__(self):
        self.chat_model = get_chat_model()

    def generate_basic_alt_text(self, image_url):
        prompt = f"Generate a clear, descriptive alt-text for the image at {image_url}."
        response = self.chat_model(prompt=prompt)
        return response 