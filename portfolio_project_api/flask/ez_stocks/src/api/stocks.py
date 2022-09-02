from flask import Blueprint, jsonify, request, abort
from ..models import Stock, db

bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@bp.route('', methods=['GET'])
def index():
    """ get all stocks """
    stocks = Stock.query.all()
    result = []
    for stock in stocks:
        result.append(stock.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    """ get 1 stock by id """
    stock = Stock.query.get_or_404(id)
    return jsonify(stock.serialize())

@bp.route('', methods=['POST'])
def create():
    """ add new stock to db """
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

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    """ delete stock from db by id"""
    stock = Stock.query.get_or_404(id)  # query for stock
    try:
        # if all goes well
        db.session.delete(stock)  # prepare DELETE statement
        db.session.commit()  # execute delete statement
        return jsonify(True)
    except:
        # if something goes wrong
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    """ update stock info """
    # check to see if stock exists
    stock = Stock.query.get_or_404(id)
    # must have name, symbol, current price, price change, and percent change in request
    if 'symbol' not in request.json or 'name' not in request.json or 'current_price' not in request.json or 'percent_change' not in request.json or 'price_change' not in request.json:
        return abort(400)

    stock.current_price = request.json['current_price']
    stock.price_change = request.json['price_change']
    stock.percent_change = request.json['percent_change']

    try:
        db.session.commit()
        return jsonify(stock.serialize())
    except:
        return jsonify(False)