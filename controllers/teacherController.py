from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from models.teacherModel import Teacher

teachers_blueprint = Blueprint('teachers', __name__)

#ROTA PARA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UM NOVO PROFESSOR
@teachers_blueprint.route('/teachers/add', methods=['GET'])
def create_teacher_page():
    return render_template('createTeacher.html')

#ROTA QUE CRIA UM NOVO PROFESSOR
@teachers_blueprint.route('/teachers', methods=['POST'])
def create_teacher():
    new_teacher = {'nome': request.form['nome'],
                          'idade': request.form['idade'],
                          'materia': request.form['materia'],
                          'observacoes': request.form['observacoes']}
    Teacher.add_teacher(new_teacher)
    return redirect(url_for('teachers.get_teachers'))

#ROTA QUE CRIA UM PROFESSOR (RETORNA JSON)
@teachers_blueprint.route('/teachers/create', methods=['POST'])
def create_teacher_json():
    new_teacher = {'nome': request.json['nome'],
                          'idade': request.json['idade'],
                          'materia': request.json['materia'],
                          'observacoes': request.json['observacoes']}
    Teacher.add_teacher(new_teacher)
    return jsonify(Teacher.get_all())

#ROTA PARA PUXAR UM PROFESSOR
@teachers_blueprint.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    try:
        teacher = Teacher.get_by_id(teacher_id)
        return render_template('teacher_id.html', teacher=teacher)
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
#ROTA PARA PUXAR UM PROFESSOR (RETORNA JSON)
@teachers_blueprint.route('/teacher/<int:teacher_id>', methods=['GET'])
def get_teacher_json(teacher_id):
    try:
        teacher = Teacher.get_by_id(teacher_id)
        return jsonify(teacher)
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404

#ROTA PARA PUXAR PROFESSORES CADASTRADOS
@teachers_blueprint.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.get_all()
    return render_template("teachers.html", teachers=teachers)

#ROTA PARA PUXAR PROFESSORES CADASTRADOS (RETORNA JSON)
@teachers_blueprint.route('/teachers/all', methods=['GET'])
def get_teachers_json():
    teachers = Teacher.get_all()
    return jsonify(teachers)

#ROTA PARA ACESSAR O FORMULÁRIO DE EDIÇÃO DE UM PROFESSOR
@teachers_blueprint.route('/teachers/<int:teacher_id>/edit', methods=['GET'])
def update_teacher_page(teacher_id):
    teacher = Teacher.get_by_id(teacher_id)
    return render_template('teacher_update.html', teacher=teacher)

#ROTA QUE EDITA O PROFESSOR
@teachers_blueprint.route('/teachers/<int:teacher_id>', methods=['PUT', 'POST'])
def update_teacher(teacher_id):
    try:
        new_data = {'nome': request.form['nome'], 
                           'idade':request.form['idade'],
                           'materia':request.form['materia'],
                           'observacoes':request.form['observacoes']}
        Teacher.update_teacher(teacher_id, new_data)
        return redirect(url_for('teachers.get_teacher', teacher_id=teacher_id))
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
#ROTA QUE EDITA O PROFESSOR (RETORNA JSON)
@teachers_blueprint.route('/teacher/<int:teacher_id>', methods=['PUT', 'POST'])
def update_teacher_json(teacher_id):
    try:
        new_data = {'nome': request.json['nome'], 
                           'idade':request.json['idade'],
                           'materia':request.json['materia'],
                           'observacoes':request.json['observacoes']}
        Teacher.update_teacher(teacher_id, new_data)
        return jsonify(Teacher.get_by_id(teacher_id))
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404

#ROTA PARA DELETAR UM PROFESSOR
@teachers_blueprint.route('/teachers/<int:teacher_id>/delete', methods=['DELETE', 'POST'])
def delete_teacher(teacher_id):
    try:
        Teacher.delete_teacher(teacher_id)
        return redirect(url_for('teachers.get_teachers'))
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
#ROTA PARA DELETAR UM PROFESSOR (RETORNA JSON)
@teachers_blueprint.route('/teacher/<int:teacher_id>/delete', methods=['DELETE', 'POST'])
def delete_teacher_json(teacher_id):
    try:
        Teacher.delete_teacher(teacher_id)
        return jsonify(Teacher.get_all())
    except Teacher.TeacherNotFound:
        return jsonify({'message': 'Professor não encontrado'}), 404
