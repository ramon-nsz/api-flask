from flask import Blueprint, jsonify, request
from models.teacher import Teacher
from dal.db import teachers

teachers_blueprint = Blueprint('teachers', __name__)

# Exemplo de como poderia ficar o cadastro após adicionar os models
#Cadastrando um professor
@teachers_blueprint.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    new_teacher = Teacher.add_teacher(data)
    return jsonify(new_teacher.to_dict()), 201


#Resgatando professores cadastrados
@teachers_blueprint.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify({'teachers': teachers})

#Atualizando dados de um professor
@teachers_blueprint.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    for teacher in teachers:
        if teacher['id'] == teacher_id:
            data = request.json
            teacher["nome"] = data.get('nome', teacher['nome'])
            teacher["idade"] = data.get('idade', teacher['idade'])
            teacher["materia"] = data.get('materia', teacher['materia'])
            teacher["observacoes"] = data.get('observacoes', teacher['observacoes'])
            return jsonify(teacher), 201
              
    return jsonify({"ERRO":"Professor não encontrado!"}), 404

#Deletando um professor
@teachers_blueprint.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teachers.remove(teacher)
            return jsonify({"mensagem":"Usuário deletado com sucesso!"}), 201
    return jsonify({"ERRO":"Usuário não encontrado!"}), 404
