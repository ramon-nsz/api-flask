from flask import Flask, request, jsonify, Blueprint
from dal.db import *
from controllers.teachers import * 
from controllers.classes import *


myApp = Flask(__name__)

myApp.register_blueprint(teachers_blueprint)
myApp.register_blueprint(classes_blueprint)



if __name__ == '__main__':
    myApp.run(debug=True)