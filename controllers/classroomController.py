from flask import Blueprint, request, jsonify,render_template,redirect, url_for
from models.classroomModel import Classroom
classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/', methods=['GET'])
def getIndex():
    return "My index"


#ROTA PARA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UMA NOVA TURMA
@classes_blueprint.route('/classes/add', methods=['GET'])
def create_classroom_page():
    return render_template('createClassroom.html')

#ROTA QUE CRIA UMA NOVA TURMA
@classes_blueprint.route('/classes', methods=['POST'])
def create_classroom():
    new_classroom = Classroom(request.form['descricao'],
                          request.form['professor'],
                          request.form['ativo'])
    Classroom.add_classroom(new_classroom)
    return redirect(url_for('classroom.get_classes'))

#ROTA PARA PUXAR UMA TURMA
@classes_blueprint.route('/classes/<int:classroom_id>', methods=['GET'])
def get_classroom(classroom_id):
    try:
        classroom = Classroom.get_by_id(classroom_id)
        return render_template('classroom_id.html', classroom=classroom)
    except Classroom.ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404

#ROTA PARA PUXAR TURMAS CADASTRADAS
@classes_blueprint.route('/classes', methods=['GET'])
def get_classes():
    classes = Classroom.get_all()
    return render_template("classes.html", classes=classes)

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
                           'professor':request.form['professor'],
                           'ativo':request.form['ativo']}
        Classroom.update_classroom(classroom_id, new_data)
        return redirect(url_for('classes.get_classroom', classroom_id=classroom_id))
    except Classroom.ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404

#ROTA PARA DELETAR UMA TURMA
@classes_blueprint.route('/classes/<int:classroom_id>/delete', methods=['DELETE', 'POST'])
def delete_classroom(classroom_id):
    try:
        Classroom.delete_classroom(classroom_id)
        return redirect(url_for('classes.get_classes'))
    except Classroom.ClassroomNotFound:
        return jsonify({'message': 'Turma não encontrada'}), 404