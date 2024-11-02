from models import get_chat_model

class BrandVoiceGenerator:
    def __init__(self):
        self.chat_model = get_chat_model()

    def integrate_brand_voice(self, image_url, brand_tone):
        prompt = (f"Generate alt-text for the image at {image_url} using a {brand_tone} tone "
                  "that aligns with Microsoft’s brand style.")
        response = self.chat_model(prompt=prompt)
        return response 