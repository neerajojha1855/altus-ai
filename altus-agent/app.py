from flask import Flask, request, jsonify
from agent.llm import generate_quiz

app = Flask(__name__)

@app.route('/generate', methods=["POST"])
def generate():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    quiz_json = generate_quiz(text)

    return jsonify(quiz_json)

if __name__ == "__main__":
    app.run(port=5001)