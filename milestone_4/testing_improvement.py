from models import get_chat_model

class TestingImprovementGenerator:
    def __init__(self):
        self.chat_model = get_chat_model()

    def refine_with_feedback(self, image_url, feedback):
        prompt = (f"Refine the alt-text for the image at {image_url} based on feedback: {feedback}.")
        response = self.chat_model(prompt=prompt)
        return response 