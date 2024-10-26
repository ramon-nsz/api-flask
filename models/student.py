from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float
from config import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(Integer, primary_key = True)
    nome = db.Column(String(120))
    idade = db.Column(Integer)
    turma_id = db.Column(Integer, ForeignKey(classroom.id))
    data_nascimento = db.Column(DateTime, timezone = True)
    nota_primeiro_semestre = db.Column(Float)
    nota_segundo_semestre = db.Column(Float)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        # Inicializa um objeto da classe Aluno
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
        students = Student.query.all()
        return [student.to_dict() for student in students]

    @staticmethod
    def get_by_id(student_id):
        student = Student.query.get(student_id)
        if not student:
            raise StudentNotFound
        return student.to_dict()



    @staticmethod
    def add_aluno(aluno_data):
        # Cria um novo aluno com os dados fornecidos, atribuindo um novo ID
        student = Student(aluno_data['nome'], 
                          aluno_data['idade'], 
                          aluno_data['turma_id'], 
                          aluno_data['data_nascimento'], 
                          aluno_data['nota_primeiro_semestre'], 
                          aluno_data['nota_segundo_semestre'])
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def update_aluno(student_id, new_data):
        student = Student.query.get(student_id)
        if not student:
            raise StudentNotFound
        student.name = new_data['name']
        db.session.commit()

    @staticmethod
    def delete_student(student_id):
        student = Student.query.get(student.id)
        if not student:
            raise StudentNotFound
        db.session.delete(student)
        db.session.commit()
       
       
class StudentNotFound(Exception):
        pass
