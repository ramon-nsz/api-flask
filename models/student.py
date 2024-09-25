from dal.db import classes
from dal.db import alunos   

class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        # Inicializa um objeto da classe Aluno
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id  # Relaciona Aluno a uma turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre

    def to_dict(self):
        # Converte o objeto Aluno para um dicionário para facilitar a serialização
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,  # ID da turma do aluno
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.calcular_media()
        }

    def calcular_media(self):
        # Calcula a média final do aluno com base nas notas dos dois semestres
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    @staticmethod
    def get_all():
        # Retorna todos os alunos na lista 'alunos', criando instâncias de Aluno
        return [Aluno(**aluno) for aluno in alunos]

    @staticmethod
    def get_by_id(aluno_id):
        # Busca um aluno pelo ID na lista 'alunos'
        for aluno in alunos:
            if aluno["id"] == aluno_id:
                return Aluno(**aluno)
        return None  # Retorna None se o aluno não for encontrado

    @staticmethod
    def add_aluno(aluno_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        new_aluno = {
            "id": len(alunos) + 1,
            "nome": aluno_data['nome'],
            "idade": aluno_data['idade'],
            "turma_id": aluno_data['turma_id'],  # Associa o aluno a uma turma
            "data_nascimento": aluno_data['data_nascimento'],
            "nota_primeiro_semestre": aluno_data['nota_primeiro_semestre'],
            "nota_segundo_semestre": aluno_data['nota_segundo_semestre']
        }
        alunos.append(new_aluno)
        return Aluno(**new_aluno)

    @staticmethod
    def update_aluno(aluno_id, data):
        # Atualiza os dados de um aluno existente pelo ID
        for aluno in alunos:
            if aluno['id'] == aluno_id:
                aluno['nome'] = data.get('nome', aluno['nome'])
                aluno['idade'] = data.get('idade', aluno['idade'])
                aluno['turma_id'] = data.get('turma_id', aluno['turma_id'])
                aluno['data_nascimento'] = data.get('data_nascimento', aluno['data_nascimento'])
                aluno['nota_primeiro_semestre'] = data.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
                aluno['nota_segundo_semestre'] = data.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
                return Aluno(**aluno)
        return None

    @staticmethod
    def delete_aluno(aluno_id):
        # Remove um aluno da lista 'alunos' pelo ID
        global alunos  # Acessa a lista global 'alunos'
        alunos = [aluno for aluno in alunos if aluno["id"] != aluno_id]
