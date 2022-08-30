from flask import Blueprint, jsonify, abort, request
from ..models import User, db

import hashlib
import secrets

def scramble(password: str):
    """ hash and salt the given password """
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix= '/users')

@bp.route('', methods=['GET'])
def index():
    users = User.query.all() # ORM performs SELECT * FROM users table
    result = []
    for user in users:
        result.append(user.serialize()) # build list of users as dictionary   
    return jsonify(result) # return JSON response

@bp.route('<int:id>', methods=['GET'])
def show(id: int):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())


@bp.route('', methods=['POST'])
def create():
    # request body must contain: name, password, and email
    if 'name' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400) # abort if requirments are not fulfilled
    # name must be > 2 chars | password must be > 7 chars
    if len(request.json['name']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # construct new user
    user = User(
        name = request.json['name'],
        password = scramble(request.json['password']),
        email = request.json['email']
    )
    db.session.add(user)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(user.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    user = User.query.get_or_404(id)  # query for user
    try:
        db.session.delete(user) # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)
