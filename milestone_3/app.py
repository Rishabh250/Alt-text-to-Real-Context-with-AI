from flask import Flask, jsonify, request
from milestone_3.accessibility_discoverability import AccessibilityDiscoverabilityGenerator

app = Flask(__name__)
generator = AccessibilityDiscoverabilityGenerator()

@app.route('/accessibility-discoverability', methods=['POST'])
def accessibility_discoverability():
    data = request.get_json()
    image_url = data.get("image_url")
    alt_text = generator.optimize_for_accessibility(image_url)
    return jsonify({"alt_text": alt_text})

if __name__ == '__main__':
    app.run(debug=True) 