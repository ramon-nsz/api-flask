from flask import Blueprint, jsonify, request
from dal.db import *

classes_blueprint = Blueprint('classes', __name__)

#Resgatando turmas
@classes_blueprint.route('/classes', methods=['GET'])
def get_class():
    return jsonify({'classes': classes})

#Cadastrando turmas
@classes_blueprint.route('/classes', methods=['POST'])
def create_classroom():
    data = request.json
    classroom = {"id": len(classes) + 1,
               "descricao":data["descricao"],
               "professor":data["professor"],
               "ativo":data["ativo"]}
    classes.append(classroom)
    return jsonify(classroom), 201

#Atualizando turmas
@classes_blueprint.route('/classes/<int:classroom_id>', methods=['PUT'])
def update_classroom(classroom_id):
    for classroom in classes:
        if classroom['id'] == classroom_id: 
            data = request.json
            classroom["descricao"] = data.get('descricao', classroom['descricao'])
            classroom["professor"] = data.get('professor', classroom['professor'])
            classroom["ativo"] = data.get('ativo', classroom['ativo'])
            return jsonify(classroom), 201
    return jsonify({"ERRO":"Turma não encontrada!"}), 404
    
#Deletando turmas
@classes_blueprint.route('/classes/<int:classroom_id>', methods=['DELETE'])
def delete_classroom(classroom_id):
    for classroom in classes:
        if classroom['id'] == classroom_id:
            classes.remove(classroom)
            return jsonify({"MENSAGEM":"Turma removida com sucesso!"}), 201
    return jsonify({"ERRO":"Turma não encontrada"}), 404