from flask import Blueprint, jsonify, abort, request
from ..models import Watch_list_stocks, db

bp = Blueprint('watch_list_stocks', __name__, url_prefix = '/watch_list_stocks')

@bp.route('', methods=['GET'])
def index():
    watch_list_stocks = Watch_list_stocks.query.all()
    result = []
    for wls in watch_list_stocks:
        result.append(wls.serialize())
    return jsonify(result)

@bp.route('/int:id>', methods=['GET'])
def show(id: int):
    wls = Watch_list_stocks.query.get_or_404(id)
    return jsonify(wls.serialize())


