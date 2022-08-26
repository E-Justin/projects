from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False, unique = True)
    date_joined = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    db.Column(
        'date_joined', db.DateTime,
        default = datetime.datetime.utcnow
    )

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'date_joined': self.date_joined
        }

class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key =  True, autoincrement = True) 
    profit_amount = db.Column(db.Float) 
    net_worth = db.Column(db.Float)

    # every portfolio must have exactly 1 user_id linked to it
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False) # FK

    def __init__(self, user_id: int):
        self.user_id = user_id
        # left out id bc it will be populated automatically'''

    def serialize(self):
        return{
            'id': self.id,
            'profit_amount': self.profit_amount,
            'net_worth': self.net_worth,
            'user_id': self.user_id
        }

class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    symbol = db.Column(db.Text, nullable = False)
    profit_amount = db.Column(db.Float)
    percent_change = db.Column(db.Float, nullable = False)
    price_change = db.Column(db.Float, nullable = False)
    current_price = db.Column(db.Float, nullable = False)
    name = db.Column(db.Text, nullable = False)
    quantity = db.Column(db.Integer)
    purchase_price = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'profit_amount': self.profit_amount,
            'percent_change': self.percent_change,
            'price_change': self.price_change,
            'current_price': self.current_price,
            'name': self.name,
            'quantity': self.quantity,
            'purchase_price': self.purchase_price
        }

class Watch_list(db.Model):
    __tablename__ = 'watch_lists'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False) #FK
    name = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'date_created': self.date_created
        }


# association table for many to many relationship btwn portfolios and stocks
class Portfolio_stocks(db.Model):
    __tablename__ = 'portfolio_stocks'
    db.metadata,
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable = False, primary_key = True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable = False, primary_key = True)

    def serialize(self):
        return{
            'portfolio_id': self.portfolio_id,
            'stock_id': self.stock_id
        }

# association table for many to many relationship btwn watch_lists and stocks
class Watch_list_stocks(db.Model):
    __tablename__ = 'watch_list_stocks'
    db.metadata,
    watch_list_id = db.Column(db.Integer, db.ForeignKey('watch_list.id'), nullable = False, primary_key = True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable = False, primary_key = True)

    def serialize(self):
        return {
            'watch_list_id': self.watch_list_id,
            'stock_id': self.stock_id
        }


