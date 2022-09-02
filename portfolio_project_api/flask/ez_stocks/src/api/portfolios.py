from flask import Blueprint, jsonify, abort, request
from ..models import Portfolio, User, db

bp = Blueprint('portfolios', __name__, url_prefix='/portfolios')

@bp.route('', methods=['GET'])
def index():
    """ get all portfolios """
    portfolios = Portfolio.query.all()
    result = []
    for p in portfolios:
        result.append(p.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    """ get portfolio from id """
    p = Portfolio.query.get_or_404(id)
    return jsonify(p.serialize())

@bp.route('', methods=['POST'])
def create():
    # request body must contain user_id
    if 'user_id' not in request.json:
        return abort(400)
    # make sure user exists
    User.query.get_or_404(request.json['user_id'])
    
    portfolio = Portfolio(
        user_id = request.json['user_id']
    )
    db.session.add(portfolio)
    db.session.commit()
    return jsonify(portfolio.serialize())

@bp.route('<int:id>', methods=['DELETE'])
def delete(id: int):
    portfolio = Portfolio.query.get_or_404(id)
    try:
        db.session.delete(portfolio)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
