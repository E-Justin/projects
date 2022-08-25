from flask import Blueprint, jsonify, abort, request
from ..models import User, db

bp = Blueprint('users', __name__, url_prefix= '/users')

@bp.route('', methods=['GET'])
def index():
    users = User.query.all() # ORM performs SELECT * FROM users table
    result = []
    for user in users:
        result.append(user.serialize()) # build list of users as dictionary   
    return jsonify(result) # return JSON response

@bp.route('', methods=['GET'])
def show(id: int):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())
