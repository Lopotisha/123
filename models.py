from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(255))
    name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))

class Account(db.Model):
    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    deposit_amount = db.Column(db.Float, nullable=True)
    deposit_term = db.Column(db.Integer, nullable=True)
    deposit_date = db.Column(db.Date, nullable=True)
    interest_rate = db.Column(db.Float, nullable=True)
