from flask import Blueprint, request, jsonify, render_template,redirect, url_for
from models.studentModel import Student

students_blueprint = Blueprint('students', __name__)

@students_blueprint.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')

#ROTA PARA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UM NOVO ALUNO
@students_blueprint.route('/students/add', methods=['GET'])
def create_student_page():
    return render_template('createStudent.html')

#ROTA QUE CRIA UM NOVO ALUNO
@students_blueprint.route('/students', methods=['POST'])
def create_student():
    new_student = {'nome': request.form['nome'],
                          'idade': request.form['idade'],
                          'turma_id': request.form['turma_id'],
                          'data_nascimento': request.form['data_nascimento'],
                          'nota_primeiro_semestre': request.form['nota_primeiro_semestre'],
                          'nota_segundo_semestre': request.form['nota_segundo_semestre']}
    Student.add_student(new_student)
    return redirect(url_for('students.get_students'))

#ROTA PARA PUXAR UM ALUNO
@students_blueprint.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
        student = Student.get_by_id(student_id)
        return render_template('student_id.html', student=student)

#ROTA PARA PUXAR ALUNOS CADASTRADOS
@students_blueprint.route('/students', methods=['GET'])
def get_students():
    students = Student.get_all()
    return render_template("students.html", students=students)

#ROTA PARA ACESSAR O FORMULÁRIO DE EDIÇÃO DE UM ALUNO
@students_blueprint.route('/students/<int:student_id>/edit', methods=['GET'])
def update_student_page(student_id):
    student = Student.get_by_id(student_id)
    return render_template('student_update.html', student=student)

#ROTA QUE EDITA O ALUNO
@students_blueprint.route('/students/<int:student_id>', methods=['PUT', 'POST'])
def update_student(student_id):
        new_data = {'nome': request.form['nome'], 
                           'idade':request.form['idade'],
                           'turma_id':request.form['turma_id'],
                           'data_nascimento':request.form['data_nascimento'],
                           'nota_primeiro_semestre': request.form['nota_primeiro_semestre'],
                           'nota_segundo_semestre': request.form['nota_segundo_semestre']}
        Student.update_student(student_id, new_data)
        return redirect(url_for('students.get_students', student_id=student_id))

#ROTA PARA DELETAR UM ALUNO
@students_blueprint.route('/students/<int:student_id>/delete', methods=['DELETE', 'POST'])
def delete_student(student_id):
        Student.delete_student(student_id)
        return redirect(url_for('students.get_students'))