from flask import Blueprint, jsonify, request
from .models import db, User, Class
from .auth import require_auth

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
