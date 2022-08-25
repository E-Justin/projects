from flask import Blueprint, jsonify, abort, request
from ..models import Portfolio, User, db

bp = Blueprint('portfolios', __name__, url_prefix='/portfolios')

@bp.route('', methods=['GET'])
def index():
    portfolios = Portfolio.query.all()
    result = []
    for p in portfolios:
        result.append(p.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Portfolio.query.get_or_404(id)
    return jsonify(p.serialize())
