from application import app, db
from sqlalchemy.sql import func
from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin 

@dataclass
class User(db.Model):
    id: int
    username: str
    name: str
    firstname: str
    gmail: str
    password: str
    cover: str

    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    gmail = db.Column(db.Integer)
    password = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f'<User {self.username}>'