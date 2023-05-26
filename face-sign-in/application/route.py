import numpy as np
import io, base64
import os, secrets
from flask_login import login_required, logout_user, login_user, current_user
from flask import abort, json
from application import app, db
from application.model import User
from flask import render_template, send_from_directory, request, flash, url_for, redirect, jsonify, Response
from PIL import Image

@app.route('/api/', methods=['POST', 'GET'])
def api():
    return render_template('video.html')


@app.route('/api/sign_up/<string:username>/<string:name>/<string:firstname>/<string:gmail>/<string:password>/', methods=['POST', 'GET'])
def api_sign_up(username, name, firstname, gmail, password):
    print(username, name, firstname, gmail, password)
    data = json.loads(request.data)
    photo = data['photo']
    image_name = save_picture(photo)
    user = User(username=username,
                name=name,
                firstname=firstname,
                gmail=gmail,
                password=password, 
                cover=image_name)
    
    return "Sing Up"

@app.route('/api/sign_in/<string:username>/<string:password>/', methods=['POST', 'GET'])
def api_sign_in(username, password):
    return f"{username}"


def save_picture(cover):
    picture_fn = secrets.token_hex(16)
    picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")

    output_size = (220, 340)
    img = Image.open(io.BytesIO(base64.b64decode(bytes(str(cover), "utf-8"))))
    img.thumbnail(output_size)
    img.save(picture_path)
    img = np.array(img)


    return f"{picture_fn}.png"

@app.route('/apip/', methods=['POST', 'GET'])
def apip():
    if request.method == 'POST':
        data = json.loads(request.data)
        photo = data['photo']
        save_picture(photo)

        return jsonify(photo)
        
    return "saas"
    

@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()