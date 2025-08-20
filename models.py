from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenoms = db.Column(db.String(50), nullable=False)
    sexe = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mdp = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.name}'"
