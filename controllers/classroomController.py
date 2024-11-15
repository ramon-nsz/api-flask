from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from models.classroomModel import Classroom, ClassroomNotFound
classes_blueprint = Blueprint('classes', __name__)

#ROTA PARA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UMA NOVA TURMA
@classes_blueprint.route('/classes/add', methods=['GET'])
def create_classroom_page():
    return render_template('createClassroom.html')

#ROTA QUE CRIA UMA NOVA TURMA
@classes_blueprint.route('/classes', methods=['POST'])
def create_classroom():
    new_classroom = {'descricao': request.form['descricao'],
                          'professor_id': request.form['professor_id'],
                          'ativo': request.form['ativo']}
    Classroom.add_classroom(new_classroom)
    return redirect(url_for('classes.get_classes'))

#ROTA QUE CRIA UMA NOVA TURMA (RETORNA JSON)
@classes_blueprint.route('/classes/create', methods=['POST'])
def create_classroom_json():
    new_classroom = {'descricao': request.json['descricao'],
                          'professor_id': request.json['professor_id'],
                          'ativo': request.json['ativo']}
    Classroom.add_classroom(new_classroom)
    return jsonify(Classroom.get_all())

#ROTA PARA PUXAR UMA TURMA
@classes_blueprint.route('/classes/<int:classroom_id>', methods=['GET'])
def get_classroom(classroom_id):
        classroom = Classroom.get_by_id(classroom_id)
        return render_template('classroom_id.html', classroom=classroom)

#ROTA PARA PUXAR UMA TURMA (RETORNA JSON)
@classes_blueprint.route('/classroom/<int:classroom_id>', methods=['GET'])
def get_classroom_json(classroom_id):
        classroom = Classroom.get_by_id(classroom_id)
        return jsonify(classroom)

#ROTA PARA PUXAR TURMAS CADASTRADAS
@classes_blueprint.route('/classes', methods=['GET'])
def get_classes():
    classes = Classroom.get_all()
    return render_template("classes.html", classes=classes)

#ROTA PARA PUXAR TURMAS CADASTRADAS (RETORNA JSON)
@classes_blueprint.route('/classes/all', methods=['GET'])
def get_classes_json():
    classes = Classroom.get_all()
    return jsonify(classes)

#ROTA PARA ACESSAR O FORMULÁRIO DE EDIÇÃO DE UMA TURMA
@classes_blueprint.route('/classes/<int:classroom_id>/edit', methods=['GET'])
def update_classroom_page(classroom_id):
    classroom = Classroom.get_by_id(classroom_id)
    return render_template('classroom_update.html', classroom=classroom)

#ROTA QUE EDITA A TURMA
@classes_blueprint.route('/classes/<int:classroom_id>', methods=['PUT', 'POST'])
def update_classroom(classroom_id):
    try:
        new_data = {'descricao': request.form['descricao'], 
                           'professor_id':request.form['professor_id'],
                           'ativo':request.form['ativo']}
        Classroom.update_classroom(classroom_id, new_data)
        return redirect(url_for('classes.get_classroom', classroom_id=classroom_id))
    except ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
#ROTA QUE EDITA A TURMA (RETORNA JSON)
@classes_blueprint.route('/classroom/<int:classroom_id>', methods=['PUT', 'POST'])
def update_classroom_json(classroom_id):
    try:
        new_data = {'descricao': request.json['descricao'], 
                           'professor_id':request.json['professor_id'],
                           'ativo':request.json['ativo']}
        Classroom.update_classroom(classroom_id, new_data)
        return jsonify(Classroom.get_by_id(classroom_id))
    except ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404

#ROTA PARA DELETAR UMA TURMA
@classes_blueprint.route('/classes/<int:classroom_id>/delete', methods=['DELETE', 'POST'])
def delete_classroom(classroom_id):
    try:
        Classroom.delete_classroom(classroom_id)
        return redirect(url_for('classes.get_classes'))
    except ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
#ROTA PARA DELETAR UMA TURMA (RETORNA JSON)
@classes_blueprint.route('/classroom/<int:classroom_id>/delete', methods=['DELETE', 'POST'])
def delete_classroom_json(classroom_id):
    try:
        Classroom.delete_classroom(classroom_id)
        return jsonify(Classroom.get_all())
    except ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404