from application import app, db
from sqlalchemy.sql import func
from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin 

@dataclass
class User(db.Model):
    id: int
    name: str
    lastname: str
    secondname: str
    gmail: str
    cover: str

    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    secondname = db.Column(db.String(100), nullable=False)
    gmail = db.Column(db.Integer)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f'<User {self.name}>'
    
@dataclass
class Colleg(db.Model):
    id: int
    collegname: str
    collegmail: str
    collegfulln: str



    id = db.Column(db.Integer, primary_key=True)
    collegname = db.Column(db.String(100), nullable=False)
    collegmail = db.Column(db.Integer)
    collegfulln = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Colleg {self.id}'
    

    