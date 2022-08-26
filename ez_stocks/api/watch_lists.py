from flask import Blueprint, jsonify, abort, request
from ..models import Watch_list, db

bp = Blueprint('watch_lists', __name__, url_prefix = '/watch_lists')

@bp.route('', methods=['GET'])
def index():
    watch_lists = Watch_list.query.all()
    result = []
    for w in watch_lists:
        result.append(w.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    w = Watch_list.query.get_or_404(id)
    return jsonify(w.serialize())
