from flask import Flask, request, jsonify
from agent.llm import generate_quiz
from agent.grader import grade_short_answer

app = Flask(__name__)

@app.route('/generate', methods=["POST"])
def generate():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    quiz_json = generate_quiz(text)

    return jsonify(quiz_json)

@app.route('/grade', methods=['POST'])
def grade():
    data = request.json
    student_answer = data.get('student_answer')
    ideal_answer = data.get('ideal_answer')
    
    result = grade_short_answer(student_answer, ideal_answer)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5001)