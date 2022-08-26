from flask import Blueprint, jsonify, request, abort
from ..models import Stock, db

bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@bp.route('', methods=['GET'])
def index():
    stocks = Stock.query.all()
    result = []
    for stock in stocks:
        result.append(stock.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    stock = Stock.query.get_or_404(id)
    return jsonify(stock.serialize())

@bp.route('', methods=['POST'])
def create():
    # request body must contain:symbol, percent_change, 
    # price_change, current_price, name
    if 'symbol' not in request.json or 'percent_change' not in request.json or 'price_change' not in request.json or 'current_price' not in request.json or 'name' not in request.json:
        return abort(400)
    stock = Stock(
        symbol = request.json['symbol'],
        percent_change = request.json['percent_change'],
        price_change = request.json['price_change'],
        current_price = request.json['current_price'],
        name = request.json['name'],
    )
    db.session.add(stock)
    db.session.commit()
    return jsonify(stock.serialize())
