import numpy as np
import io, base64
import os, secrets
from flask_login import login_required, logout_user, login_user, current_user
from flask import abort, json
from application import app, db
from application.model import User, Colleg
from flask import render_template, send_from_directory, request, flash, url_for, redirect, jsonify, Response
from flask_cors import cross_origin
from PIL import Image

tokenapi=["hackback-l8QREcXUYwT9!Q0mZcZJe1CAfVoF8B41APTNQp8CHiZLchrpDMrV52s",
"hackbackecTz3z7rPBUSVehqKs2vxTVTJIAzpei38MrnOnx9b?9ZXJMAcWLvmhga",
"hackbackbos3dV4xYHso=PPMVVOE4eB/LUwjmTmzODgowCehJkIEI-tTpWCuD!YN",
"hackbackM74N=dIVx/=Z7Aj/L7qgkYBgWc4p57N7dxkeKr1m!RKpol51jcafYD/Y",]

collegname = ["АМБК", "АМСТК", "АГПК", "АМК", "АКМГПК", "ГККП"]
collegmail = ["info@ambk.kz", "info@agknt.kz", "info@agpk.kz", "volcharazack@gmail.com", "pedkol1@list.ru", "agke_i_et@mail.ru"]
collegfulln = ["Алматы-мемлекеттік-бизнес-коледжі",
                "Алматы-мемлекеттік-сервис-жане-технологиялар-коледжі",
                "Алматы-мемлекеттік-политехникалык-колледжі",
                "Алматинский-многопрофильный-колледж",
                "Алматы-казак-мемлекеттік-гуманитарлык-педагогтік-коледжі",
                "Алматинский-государственный-колледж-энергетики-и-электронных-технологий"]


@app.route('/api/<string:token>/<string:name>/<string:lastname>/<string:secondname>/<string:gmail>/<string:colleg>/', methods=['POST', 'GET'])
def api(token, name, lastname, secondname, gmail, colleg):
    if token in tokenapi:
        data = Colleg.query.all()
        return f"{name}, {lastname}, {secondname}, {gmail}, {colleg}"

@app.route('/export/', methods=['POST', 'GET'])
@cross_origin()
def data():
    token = request.args.get('token')
    if token in tokenapi:
        data = Colleg.query.all()
        data = jsonify(data)
        #data.headers.add('Access-Control-Allow-Origin', '*')
        return data
    else:
        return "no no no non on on on "

  
@app.route('/export/<string:token>/<int:id>/', methods=['POST', 'GET'])
def get_by_id(token, id):
    if token in tokenapi:
        data = Colleg.query.get_or_404(id)
        return jsonify(data)

"""@app.route('/export/<string:token>/<string:name>/', methods=['POST', 'GET'])
def get_by_name(token, name):
    if token in tokenapi: 
        sddd = request.args.get('user')
        data = Colleg.query.get_or_404(name)
        return jsonify(name)"""

@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()

    for i in zip(collegname, collegmail, collegfulln):
        colleg = Colleg(collegname=i[0],
                        collegmail=i[1],
                        collegfulln=i[2])
        db.session.add(colleg)
        db.session.commit()

