from flask import Blueprint, request, jsonify
from models import Item, db

items_bp = Blueprint('items', __name__)

@items_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@items_bp.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'], effect=data['effect'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201
