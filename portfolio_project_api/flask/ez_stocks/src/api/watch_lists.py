from flask import Blueprint, jsonify, abort, request
from ..models import Watch_list, User, db

bp = Blueprint('watch_lists', __name__, url_prefix = '/watch_lists')

@bp.route('', methods=['GET'])
def index():
    """ get all watch_lists """
    watch_lists = Watch_list.query.all()
    result = []
    for w in watch_lists:
        result.append(w.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    """ get one watch list by /id"""
    w = Watch_list.query.get_or_404(id)
    return jsonify(w.serialize())

@bp.route('', methods=['POST'])
def create():
    """ create new watch list """
    # request body must contain a watch list name and user id
    if 'name' not in request.json or 'user_id' not in request.json:
        return abort(400)
    # user with matching id must exist - else: throw 404 status code
    User.query.get_or_404(request.json['user_id'])
    # construct new watchlist
    wl = Watch_list(
        name = request.json['name'],
        user_id = request.json['user_id']
    )
    db.session.add(wl)
    db.session.commit()
    return jsonify(wl.serialize())

@bp.route('<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    """ update watch list (change name)"""
    # request body must contain id, name, and user_id
    if 'user_id' not in request.json or 'id' not in request.json or 'name' not in request.json:
        return abort(400)
    # make sure watch_list exists, get it if so
    wl = Watch_list.query.get_or_404(id)

    wl.name = request.json['name']

    db.session.commit()
    return jsonify(wl.serialize())

