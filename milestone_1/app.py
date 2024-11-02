from flask import Flask, jsonify, request
from milestone_1.alt_text_generator import AltTextGenerator

app = Flask(__name__)
generator = AltTextGenerator()

@app.route('/generate-alt-text', methods=['POST'])
def generate_alt_text():
    data = request.get_json()
    image_url = data.get("image_url")
    alt_text = generator.generate_basic_alt_text(image_url)
    return jsonify({"alt_text": alt_text})

if __name__ == '__main__':
    app.run(debug=True) 