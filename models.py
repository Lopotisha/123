from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(255))
    name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
