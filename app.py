from flask import Flask
from config import myApp,db
from controllers.teacherController import teachers_blueprint
from controllers.classroomController import classes_blueprint
from controllers.studentController import students_blueprint

myApp.register_blueprint(teachers_blueprint)
myApp.register_blueprint(classes_blueprint)
myApp.register_blueprint(students_blueprint)


with myApp.app_context():
    db.create_all()

if __name__ == '__main__':
    myApp.run(host=myApp.config["HOST"], port = myApp.config['PORT'],debug=myApp.config['DEBUG'] )