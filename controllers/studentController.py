from flask import Blueprint, request, jsonify, render_template,redirect, url_for
from models.studentModel import Student
from services.valid_date import valid_date

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

#ROTA QUE CRIA UM NOVO ALUNO (RETORNA JSON)
@students_blueprint.route('/students/create', methods=['POST'])
def create_student_json():
    valid_birth_date = valid_date(request.json['data_nascimento'])
    if not valid_birth_date:
          return jsonify({"ERRO":"Data de nascimento inválida. Use o formato YYYY-MM-DD."})
    else:
        new_student = {'nome': request.json['nome'],
                            'idade': request.json['idade'],
                            'turma_id': request.json['turma_id'],
                            'data_nascimento': request.json['data_nascimento'],
                            'nota_primeiro_semestre': request.json['nota_primeiro_semestre'],
                            'nota_segundo_semestre': request.json['nota_segundo_semestre']}
        Student.add_student(new_student)
        return jsonify(Student.get_all())

#ROTA PARA PUXAR UM ALUNO
@students_blueprint.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
        student = Student.get_by_id(student_id)
        return render_template('student_id.html', student=student)

#ROTA PARA PUXAR UM ALUNO (RETORNA JSON)
@students_blueprint.route('/student/<int:student_id>', methods=['GET'])
def get_student_json(student_id):
        student = Student.get_by_id(student_id)
        return jsonify(student)

#ROTA PARA PUXAR ALUNOS CADASTRADOS
@students_blueprint.route('/students', methods=['GET'])
def get_students():
    students = Student.get_all()
    return render_template("students.html", students=students)

#ROTA PARA PUXAR ALUNOS CADASTRADOS (RETORNA JSON)
@students_blueprint.route('/students/all', methods=['GET'])
def get_students_json():
    students = Student.get_all()
    return jsonify(students)

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

#ROTA QUE EDITA O ALUNO (RETORNA JSON)
@students_blueprint.route('/student/<int:student_id>', methods=['PUT', 'POST'])
def update_student_json(student_id):
        new_data = {'nome': request.json['nome'], 
                           'idade':request.json['idade'],
                           'turma_id':request.json['turma_id'],
                           'data_nascimento':request.json['data_nascimento'],
                           'nota_primeiro_semestre': request.json['nota_primeiro_semestre'],
                           'nota_segundo_semestre': request.json['nota_segundo_semestre']}
        Student.update_student(student_id, new_data)
        return jsonify(Student.get_by_id(student_id))

#ROTA PARA DELETAR UM ALUNO
@students_blueprint.route('/students/<int:student_id>/delete', methods=['DELETE', 'POST'])
def delete_student(student_id):
        Student.delete_student(student_id)
        return redirect(url_for('students.get_students'))

#ROTA PARA DELETAR UM ALUNO (RETORNA JSON)
@students_blueprint.route('/student/<int:student_id>/delete', methods=['DELETE', 'POST'])
def delete_student_json(student_id):
        Student.delete_student(student_id)
        return jsonify(Student.get_all())