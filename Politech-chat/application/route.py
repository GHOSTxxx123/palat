from flask import render_template, flash, redirect, url_for, session, request, logging
from flask_login import login_required, login_user, logout_user
from passlib.hash import sha256_crypt
from functools import wraps

from application import app, db
from application.models import User, Message
from application.forms import Sign_in, Sign_up, MessageForm




@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sign_in/', methods=('GET', 'POST'))
def sign_in():
    form = Sign_in()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        password = db.session.query(User).filter(User.password == form.password.data).first()
        if user and password:
            online = User.query.get_or_404(user.id)
            online.online = True
            uid = user.id
            name = user.username
            session['logged_in'] = True
            session['uid'] = uid
            session['s_name'] = name
            db.session.commit()
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))

    return render_template('sign_in.html', form=form)

@app.route('/sign_up/', methods=['POST', 'GET'])
def sign_up():
    form = Sign_up()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    firstname=form.firstname.data,
                    username = form.username.data,
                    gmail=form.gmail.data,
                    password=form.password.data,
                    kyrs=form.kyrs.data)
        db.session.add(user)
        db.session.commit()   
        print(form.username.data, form.password.data)     
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', form=form)


@app.route('/chatting/<int:id>/', methods=['GET', 'POST'])
@login_required
def chatting(id):
    if 'uid' in session:
        chat = User.query.all()
        form = MessageForm()
        user_id = db.session.query(User).filter(User.id == id).first()
        if user_id:
            session['name'] = user_id.username
            uid = session['uid']
            session['lid'] = id
            if  form.validate_on_submit():
                messa = Message(body=form.body.data,
                                msg_by=id,
                                msg_to=uid)
                db.session.add(messa)
                db.session.commit()
            return render_template('chat_room.html', form=form, users=chat)
    return redirect(url_for('sign_in'))
    


@app.route('/chats/', methods=['GET', 'POST'])
@login_required
def chats():
    form = MessageForm()
    if 'lid' in session:
        id = session['lid']
        uid = session['uid']
        get_1 = db.session.query(Message).filter().first()
        chat = Message.query.all()


    return render_template('chats.html', chat=chat)


@app.route('/logout/')
@login_required
def logout():
    id = session['lid']
    online = User.query.get_or_404(id)
    online.online = False
    db.session.commit()
    logout_user()
    return redirect(url_for('sign_in'))


@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()