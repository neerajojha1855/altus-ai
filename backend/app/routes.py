import requests
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload
from functools import wraps
from .models import db, User, Class, Quiz, Submission, Assignment
from .auth import require_auth
from .notifications import send_remainder_email

AGENT_URL = "http://localhost:5001"

api = Blueprint('api', __name__)

def require_role(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            firebase_uid = request.user.get('uid')
            user = User.query.filter_by(firebase_uid=firebase_uid).first()
            if not user or user.role not in roles:
                return jsonify({"error": f"Unauthorized. Requires role: {', '.join(roles)}"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@api.route('/users', methods=["POST"])
@require_auth
def create_user():
    firebase_uid = request.user.get('uid')
    data = request.json
    
    user = User.query.filter_by(firebase_uid=firebase_uid).first()
    if user:
        return jsonify({"message": "User already exists", "id": user.id}), 200
        
    new_user = User(
        firebase_uid=firebase_uid,
        email=data.get('email'),
        name=data.get('name', 'User'),
        role=data.get('role', 'student')
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created", "id": new_user.id}), 201

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
        "name": user.name,
        "role": user.role
    })

@api.route('/classes', methods=["POST"])
@require_auth
@require_role(['teacher', 'administrator'])
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
@require_role(['student'])
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

@api.route('/assignment/<int:assignment_id>/tracking', methods=["GET"])
@require_auth
@require_role(['teacher', 'administrator'])
def get_submission_tracking(assignment_id):
    assignment = Assignment.query.get(assignment_id)
    class_id = assignment.class_id

    students = User.query.join(student_classes).filter(student_classes.c.class_id == class_id).all()

    quiz = Quiz.query.filter_by(assignment_id=assignment_id).first()
    submissions = Submission.query.filter_by(quiz_id=quiz.id).all()
    submitted_student_ids = {s.student_id for s in submissions}

    tracking_data = []
    for student in students:
        status = "submitted" if student.id in submitted_student_ids else "missing"
        tracking_data.append({
            "student_id": student.id,
            "student_name": student.name,
            "student_email": student.email,
            "status": status
        })
    
    return jsonify(tracking_data)

@api.route('/assignments/<int:assigment_id>/remind', methods=["POST"])
@require_auth
@require_role(['teacher', 'administrator'])
def send_remainder(assigment_id):
    data = request.json
    student_ids = data.get('student_ids', [])

    assignemnt = Assignment.query.get(assigment_id)
    students = User.query.filter_by(User.id.in_(student_ids)).all()

    for student in students:
        send_remainder_email(student.email, student.name, assignment_title)
    
    return jsonify({
        "message": f"Sent {len(students)} remainders."
    })