from flask import Flask, jsonify, request
from milestone_4.testing_improvement import TestingImprovementGenerator

app = Flask(__name__)
generator = TestingImprovementGenerator()

@app.route('/testing-improvement', methods=['POST'])
def testing_improvement():
    data = request.get_json()
    image_url = data.get("image_url")
    feedback = data.get("feedback")
    refined_text = generator.refine_with_feedback(image_url, feedback)
    return jsonify({"refined_text": refined_text})

if __name__ == '__main__':
    app.run(debug=True) 