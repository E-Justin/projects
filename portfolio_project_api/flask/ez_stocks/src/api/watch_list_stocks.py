from flask import Blueprint, jsonify, abort, request
from ..models import Watch_list_stocks,db, Watch_list, Stock

bp = Blueprint('watch_list_stocks', __name__, url_prefix = '/watch_list_stocks')

@bp.route('', methods=['GET'])
def index():
    watch_list_stocks = Watch_list_stocks.query.all()
    result = []
    for wls in watch_list_stocks:
        result.append(wls.serialize())
    return jsonify(result)

@bp.route('', methods=['POST'])
def create():
    """ add stock to watch_list through association table"""
    # request must contain watch_list_id and stock_id
    if 'watch_list_id' not in request.json or 'stock_id' not in request.json:
        return abort(400)
    # check if watch_list_id exists
    Watch_list.query.get_or_404(request.json['watch_list_id'])
    # check if stock_id exists
    Stock.query.get_or_404(request.json['stock_id']) 
    # construct watch_list_stocks
    wls = Watch_list_stocks(
        watch_list_id = request.json['watch_list_id'],
        stock_id = request.json['stock_id']
    )
    db.session.add(wls)
    db.session.commit()
    return jsonify(wls.serialize())




