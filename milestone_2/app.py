from flask import Flask, jsonify, request
from milestone_2.brand_voice_generator import BrandVoiceGenerator

app = Flask(__name__)
generator = BrandVoiceGenerator()

@app.route('/brand-voice', methods=['POST'])
def brand_voice_integration():
    data = request.get_json()
    image_url = data.get("image_url")
    brand_tone = data.get("brand_tone")
    alt_text = generator.integrate_brand_voice(image_url, brand_tone)
    return jsonify({"alt_text": alt_text})

if __name__ == '__main__':
    app.run(debug=True) 