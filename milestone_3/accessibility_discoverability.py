from models import get_chat_model

class AccessibilityDiscoverabilityGenerator:
    def __init__(self):
        self.chat_model = get_chat_model()

    def optimize_for_accessibility(self, image_url):
        prompt = (f"Generate alt-text for the image at {image_url} optimized for accessibility and discoverability.")
        response = self.chat_model(prompt=prompt)
        return response 