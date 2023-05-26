from application import app, db
from sqlalchemy.sql import func
from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin 

@dataclass
class Message(db.Model):
    __tablename__ = 'message'
    id: int
    body: str
    msg_by: str
    msg_to: str
    msg_time: int

    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
    msg_by = db.Column(db.String(100), nullable=False)
    msg_to = db.Column(db.String(100), nullable=False)
    msg_time = db.Column(db.DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return f'<Message {self.body}>'



@app.login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@dataclass
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: int
    name: str
    firstname: str
    gmail: str
    password: str
    kyrs: int
    created_on: str
    updated_on: str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    gmail = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    kyrs = db.Column(db.Integer)
    online = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,  onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'
