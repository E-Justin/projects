from flask import Blueprint, jsonify, request, abort
from ..models import Stock, db
from src import stock_info

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

'''@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
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
        return jsonify(False)'''

@bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
def update(id: int):
    """ update stock info by web scraping from id number"""
    # check to see if stock exists -> get it if there
    stock = Stock.query.get_or_404(id)
    # must have name, symbol, current price, price change, and percent change in request
    if 'symbol' not in request.json or 'name' not in request.json or 'current_price' not in request.json or 'percent_change' not in request.json or 'price_change' not in request.json:
        return abort(400)

    # the following function returns data in this format as a list of strings: [stock_price, price_change, percent_change]
    data = stock_info.get_stock_info(id)
    
    # update stock info
    stock.current_price = float(data[0])
    stock.price_change  = float(data[1])
    stock.percent_change = float(data[2])

    try: # if all goes well
        db.session.commit()  # commit the changes
        return jsonify(stock.serialize())  # return the stock info as json
    except: # if something goes wrong
        return jsonify(False)
