from flask import jsonify, request
from app.models.user_model import User
from app import db

def get_users(): # busca todos os usuarios da base
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

def get_user(user_id): # busca usuario por id
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict()), 200

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

