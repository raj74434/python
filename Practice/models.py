from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone=db.Column(db.String(10), unique=True, nullable=False)
    refer=db.Column(db.String(7), nullable=True)
    password = db.Column(db.String(100), nullable=False)
