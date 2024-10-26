from config import db

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(120))
    observacoes = db.Column(db.String(120))

    def __init__(self, nome, idade, materia, observacoes):
        # Inicializa um objeto da classe Teacher com os atributos id, nome, idade, materia e observacoes
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
        teachers = Teacher.query.all()
        return [teacher.to_dict() for teacher in teachers]

    @staticmethod
    def get_by_id(teacher_id):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise TeacherNotFound
        return teacher.to_dict()

    @staticmethod
    def add_teacher(teacher_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        new_teacher = Teacher(teacher_data['nome'], 
                          teacher_data['idade'], 
                          teacher_data['materia'], 
                          teacher_data['observacoes'])
        db.session.add(new_teacher)
        db.session.commit()

    @staticmethod
    def update_teacher(teacher_id, new_data):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise TeacherNotFound
        teacher.name = new_data['name']
        db.session.commit()

    @staticmethod
    def delete_teacher(teacher_id):
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise TeacherNotFound
        db.session.delete(teacher)
        db.session.commit()

class TeacherNotFound(Exception):
        pass
