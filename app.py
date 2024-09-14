from flask import Flask, jsonify, request
from teachers import teachers

myApp = Flask(__name__)

# To-do list:

#  - CREATE (método POST): OK
#  - READ (método GET): OK
#  - UPDATE (método PUT): OK
#  - DELETE (método DELETE): OK

@myApp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    teacher = {
        'id': len(teachers) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacoes': data['observacoes']
    }
    teachers.append(teacher)
    return jsonify(teacher), 201

@myApp.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify({'teachers': teachers})

@myApp.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    for teacher in teachers:
        if teacher['id'] == teacher_id:
            data = request.json
            teacher['nome'] = data.get('nome', teacher['nome'])
            teacher['idade'] = data.get('idade', teacher['idade'])
            teacher['materia'] = data.get('materia', teacher['materia'])
            teacher['observacoes'] = data.get('observacoes', teacher['observacoes'])
            return jsonify(teacher), 201
        
        return jsonify({"ERRO":"Professor não encontrado!"}), 404

@myApp.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    for teacher in teachers:
        if teacher['id'] == teacher_id:
            teachers.remove(teacher)
            return jsonify({"mensagem":"Usuário deletado com sucesso!"}), 201
    return jsonify({"ERRO":"Usuário não encontrado!"}), 404


if __name__ == '__main__':
    myApp.run(debug=True)