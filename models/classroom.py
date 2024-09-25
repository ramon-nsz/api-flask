from dal.db import classes 

class Classroom:
    def __init__(self, id, descricao, professor, ativo):
        # Inicializa um objeto da classe Classroom com os atributos id, descricao, professor e ativo
        self.id = id
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        # Converte o objeto Classroom para um dicionário
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor": self.professor,
            "ativo": self.ativo
        }

    @staticmethod
    def get_all():
        # Retorna todas as turmas (classrooms) na lista 'classes', criando instâncias de Classroom
        return [Classroom(**classroom) for classroom in classes]

    @staticmethod
    def get_by_id(classroom_id):
        # Busca uma turma pelo ID na lista 'classes'
        for classroom in classes:
            if classroom["id"] == classroom_id:
                # Retorna uma instância de Classroom se o ID for encontrado
                return Classroom(**classroom)
        # Retorna None se a turma não for encontrada
        return None

    @staticmethod
    def add_classroom(classroom_data):
        # Cria uma nova turma com os dados fornecidos, atribuindo um novo ID
        new_classroom = {
            "id": len(classes) + 1,  # Define o ID como o próximo número disponível
            "descricao": classroom_data['descricao'],
            "professor": classroom_data['professor'],
            "ativo": classroom_data['ativo']
        }
        # Adiciona a nova turma à lista 'classes'
        classes.append(new_classroom)
        # Retorna uma instância de Classroom com os dados da nova turma
        return Classroom(**new_classroom)

    @staticmethod
    def update_classroom(classroom_id, data):
        # Atualiza os dados de uma turma existente pelo ID
        for classroom in classes:
            if classroom['id'] == classroom_id:
                # Atualiza os campos fornecidos (se houver) nos dados recebidos
                classroom['descricao'] = data.get('descricao', classroom['descricao'])
                classroom['professor'] = data.get('professor', classroom['professor'])
                classroom['ativo'] = data.get('ativo', classroom['ativo'])
                # Retorna a instância de Classroom atualizada
                return Classroom(**classroom)
        # Retorna None se a turma com o ID fornecido não for encontrada
        return None

    @staticmethod
    def delete_classroom(classroom_id):
        # Remove uma turma da lista 'classes' pelo ID
        global classes  # Acessa a lista global 'classes'
        classes = [classroom for classroom in classes if classroom["id"] != classroom_id]
