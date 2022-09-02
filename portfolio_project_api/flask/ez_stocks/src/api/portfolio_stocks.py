from flask import Blueprint, jsonify, abort, request
from ..models import Portfolio_stocks, db

bp = Blueprint('portfolio_stocks', __name__, url_prefix = '/portfolio_stocks')

@bp.route('', methods=['GET'])
def index():
    portfolio_stocks = Portfolio_stocks.query.all()
    result = []
    for ps in portfolio_stocks:
        result.append(ps.serialize())
    return jsonify(result)



