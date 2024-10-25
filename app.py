import os
from flask import Flask, request, jsonify, Blueprint
from config import app,db
from controllers.teachers import * 
from controllers.classes import *


myApp = Flask(__name__)

myApp.register_blueprint(teachers_blueprint)
myApp.register_blueprint(classes_blueprint)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )