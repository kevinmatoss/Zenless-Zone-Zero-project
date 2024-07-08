from flask import Blueprint, request, jsonify
from models import Character, db

characters_bp = Blueprint('characters', __name__)

@characters_bp.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.to_dict() for character in characters])

@characters_bp.route('/characters', methods=['POST'])
def add_character():
    data = request.get_json()
    new_character = Character(name=data['name'], description=data['description'])
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.to_dict()), 201
