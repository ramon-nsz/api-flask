from flask import Flask, request, jsonify
from dal.db import *

myApp = Flask(__name__)

#Cadastrando um professor
@myApp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    teacher = {"id": len(teachers) + 1,
               "nome":data["nome"], 
               "idade":data["idade"],
               "materia":data["materia"], 
               "observacoes":data["observacoes"]
               }
    teachers.append(teacher)
    return jsonify(teacher), 201

#Resgatando professores cadastrados
@myApp.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify({'teachers': teachers})

#Atualizando dados de um professor
@myApp.route('/teachers/<int:teacher_id>', methods=['PUT'])
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
@myApp.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teachers.remove(teacher)
            return jsonify({"mensagem":"Usuário deletado com sucesso!"}), 201
    return jsonify({"ERRO":"Usuário não encontrado!"}), 404

#Resgatando turmas
@myApp.route('/classes', methods=['GET'])
def get_class():
    return jsonify({'classes': classes})

#Cadastrando turmas
@myApp.route('/classes', methods=['POST'])
def create_classroom():
    data = request.json
    classroom = {"id": len(classes) + 1,
               "descricao":data["descricao"],
               "professor":data["professor"],
               "ativo":data["ativo"]}
    classes.append(classroom)
    return jsonify(classroom), 201

#Atualizando turmas
@myApp.route('/classes/<int:classroom_id>', methods=['PUT'])
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
@myApp.route('/classes/<int:classroom_id>', methods=['DELETE'])
def delete_classroom(classroom_id):
    for classroom in classes:
        if classroom['id'] == classroom_id:
            classes.remove(classroom)
            return jsonify({"MENSAGEM":"Turma removida com sucesso!"}), 201
    return jsonify({"ERRO":"Turma não encontrada"}), 404

if __name__ == '__main__':
    myApp.run(debug=True)