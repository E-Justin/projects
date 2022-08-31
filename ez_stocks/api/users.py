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
    """ get all users """
    users = User.query.all() # ORM performs SELECT * FROM users table
    result = []
    for user in users:
        result.append(user.serialize()) # build list of users as dictionary   
    return jsonify(result) # return JSON response

@bp.route('<int:id>', methods=['GET'])
def show(id: int):
    """ get 1 user from id """
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())


@bp.route('', methods=['POST'])
def create():
    """ create new user"""
    # request body must contain: name, password, and email
    if 'name' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400) # abort if requirments are not fulfilled
    # name must be > 2 chars | password must be > 7 chars
    if len(request.json['name']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # construct new user
    user = User(
        name = request.json['name'],
        password = scramble(request.json['password']), # encrypt password before storing in db
        email = request.json['email']
    )
    db.session.add(user)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(user.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    """ delete user from id """
    user = User.query.get_or_404(id)  # query for user
    try:
        db.session.delete(user) # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

@bp.route('/<int:id>', methods = ['PATCH', 'PUT'])
def update(id:int):
    """ update user info 
        can update username, pw, or both """
    # check to see if user exists
    user = User.query.get_or_404(id)
    # name and pw must be in request
    if 'name' not in request.json and 'password' not in request.json and 'email' not in request.json:
        return abort(400)
    
    if 'name' in request.json:
        # name must be at least 3 characters long
        if len(request.json['name']) < 3:
            # if name is too short (> 3)
            return abort(400)
        else: # if name is appropriate length
            # update name
            user.name = request.json['name']
    
    if 'password' in request.json:
    # pw must be at least 8 characters long
        if len(request.json['password']) < 8:
            # if pw is not long enough
            return abort(400)
        else:
            # encrypt password and store to db
            user.password = scramble(request.json['password'])

    if 'email' in request.json:
        if not '@' in request.json['email']:
            # email must have @ to be valid
            return abort(400)
        else:
            # update pw
            user.email = request.json['email']

    
    try: # if everything goes well
        # commit change
        db.session.commit()
        return jsonify(user.serialize())
    except:
        # if something went wrong
        return jsonify(False)

