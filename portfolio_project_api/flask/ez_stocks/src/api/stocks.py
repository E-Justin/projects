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
    """ add new stock to db and web scrape current price and other info """
    # request body must contain stock symbol
    if 'symbol' not in request.json:
        return abort(400)

    # the following function returns data in this format as a list of strings: ['The Walt Disney Company', '112.73', '+0.04', '+0.04']
    data = stock_info.get_stock_info_by_symbol(request.json['symbol'])

    # create new Stock object
    stock = Stock(
        name = data[0],
        symbol = request.json['symbol'],
        current_price = float(data[1]),
        price_change = float(data[2]),
        percent_change = float(data[3])
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


@bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
def update(id: int):
    """ update stock info by web scraping from id number"""
    # check to see if stock exists -> get it if there
    stock = Stock.query.get_or_404(id)

    # the following function returns data in this format as a list of strings: [stock_price, price_change, percent_change]
    data = stock_info.get_stock_info_by_pk(id)

    # update stock info
    stock.current_price = float(data[0])
    stock.price_change  = float(data[1])
    stock.percent_change = float(data[2])

    try: 
        db.session.commit()
        return jsonify(stock.serialize())
    except: 
        return jsonify(False)
