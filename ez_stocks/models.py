from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False, unique = True)
    date_joined = db.Column(db.DateTime, default = datetime.datetime.utcnow, nullable = False)

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
    profit_amount = db.Column(db.Numeric) 
    net_worth = db.Column(db.Numeric)

    # every portfolio must have exactly 1 user_id linked to it
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

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
