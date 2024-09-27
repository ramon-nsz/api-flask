from dal.db import teachers 

class Teacher:
    def __init__(self, id, nome, idade, materia, observacoes):
        # Inicializa um objeto da classe Teacher com os atributos id, nome, idade, materia e observacoes
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        # Converte o objeto Teacher para um dicionário
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
        }

    @staticmethod
    def get_all():
        # Retorna todos os professores na lista 'teachers', criando instâncias de Teacher para cada um
        return [Teacher(**teacher) for teacher in teachers]

    @staticmethod
    def get_by_id(teacher_id):
        # Busca um professor pelo ID na lista 'teachers'
        for teacher in teachers:
            if teacher["id"] == teacher_id:
                # Retorna uma instância de Teacher se o ID for encontrado
                return Teacher(**teacher)
        # Retorna None se o professor não for encontrado
        return None

    @staticmethod
    def add_teacher(teacher_data):
        # Cria um novo professor com os dados fornecidos, atribuindo um novo ID
        new_teacher = {
            "id": len(teachers) + 1,  # Define o ID como o próximo número na sequência
            "nome": teacher_data['nome'],
            "idade": teacher_data['idade'],
            "materia": teacher_data['materia'],
            "observacoes": teacher_data.get('observacoes', '')  # Se 'observacoes' não for fornecido, usa uma string vazia
        }
        # Adiciona o novo professor à lista de professores
        teachers.append(new_teacher)
        # Retorna uma instância de Teacher com os dados do novo professor
        return Teacher(**new_teacher)

    @staticmethod
    def update_teacher(teacher_id, data):
        # Atualiza os dados de um professor existente pelo ID
        for teacher in teachers:
            if teacher['id'] == teacher_id:
                # Atualiza os campos fornecidos (se houver) nos dados recebidos
                teacher['nome'] = data.get('nome', teacher['nome'])
                teacher['idade'] = data.get('idade', teacher['idade'])
                teacher['materia'] = data.get('materia', teacher['materia'])
                teacher['observacoes'] = data.get('observacoes', teacher['observacoes'])
                # Retorna a instância de Teacher atualizada
                return Teacher(**teacher)
        # Retorna None se o professor com o ID fornecido não for encontrado
        return None

    @staticmethod
    def delete_teacher(teacher_id):
        # Remove um professor da lista 'teachers' pelo ID
        global teachers  # Acessa a lista global de professores
        teachers = [teacher for teacher in teachers if teacher["id"] != teacher_id]
        # A lista 'teachers' é atualizada removendo o professor com o ID correspondente
