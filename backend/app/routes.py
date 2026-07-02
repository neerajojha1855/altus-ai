import requests
from flask import Blueprint, jsonify, request
from .models import db, User, Class
from .auth import require_auth

AGENT_URL = "http://localhost:5001"

api = Blueprint('api', __name__)

@api.route('/users/me', methods=["GET"])
@require_auth
def get_me():
    firebase_uid = request.user.get('uid')
    user = User.query.filter_by(firebase_uid=firebase_uid).first()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role
    })

@api.route('/classes', methods=["POST"])
@require_auth
def create_class():
    data = request.json
    firebase_uid = request.user.get('uid')
    user = User.query.filter_by(firebase_uid=firebase_uid).first()

    new_class = Class(teacher_id=user.id, name=data['name'], subject=data.get('subject'))
    db.session.add(new_class)
    db.session.commit()

    return jsonify({
        "id": new_class.id,
        "name": new_class.name
    }), 201

@api.route('/quizzes/<int:quiz_id>/submit', methods=['POST'])
@require_auth
def submit_quiz(quiz_id):
    student_uid = request.user.get('uid')
    student = User.query.filter_by(firebase_uid=student_uid).first()
    
    data = request.json
    student_answers = data.get('answers') # List of answers
    
    quiz = Quiz.query.get(quiz_id)
    questions = quiz.questions_json
    
    total_score = 0
    feedback = []
    
    # Simple Auto-grading loop
    for i, q in enumerate(questions['mcq']):
        if student_answers.get(f"mcq_{i}") == q['correct_answer']:
            total_score += 1
            feedback.append({"type": "mcq", "correct": True})
        else:
            feedback.append({"type": "mcq", "correct": False})
            
    for i, q in enumerate(questions['short_answer']):
        s_ans = student_answers.get(f"short_{i}", "")
        # Call Agent to grade
        res = requests.post(f"{AGENT_URL}/grade", json={
            "student_answer": s_ans,
            "ideal_answer": q['ideal_answer']
        })
        grade_data = res.json()
        total_score += grade_data['score']
        feedback.append({"type": "short", "score": grade_data['score'], "feedback": grade_data['feedback']})
        
    submission = Submission(
        quiz_id=quiz_id,
        student_id=student.id,
        answers_json=student_answers,
        score=total_score,
        ai_feedback=feedback
    )
    db.session.add(submission)
    db.session.commit()
    
    return jsonify({
        "message": "Submitted",
        "score": total_score,
        "feedback": feedback
    })