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


@bp.route('', methods=['POST'])
def create():
    # request body must contain: name, password, and email
    if 'name' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400) # abort if requirments are not fulfilled
    # construct new user
    user = User(
        name = request.json['name'],
        password = request.json['password'],
        email = request.json['email']
    )
    db.session.add(user)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(user.serialize())
