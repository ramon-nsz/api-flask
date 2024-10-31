from config import db 

class Classroom(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(120))
    professor = db.Column(db.String(120))
    ativo = db.Column(db.String, default = True)

    def __init__(self, descricao, professor, ativo):
        # Inicializa um objeto da classe Classroom com os atributos id, descricao, professor e ativo
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
        classes = Classroom.query.all()
        return [classroom.to_dict() for classroom in classes]


    @staticmethod
    def get_by_id(classroom_id):
       classroom = Classroom.query.get(classroom_id)
       if not classroom:
           raise ClassroomNotFound
       return classroom.to_dict()
           

    @staticmethod
    def add_classroom(classroom_data):
        # Cria uma nova turma com os dados fornecidos, atribuindo um novo ID
        classroom = Classroom(classroom_data['descricao'],
                              classroom_data['professor'],
                              classroom_data['ativo'])
        db.session.add(classroom)
        db.session.commit()

    @staticmethod
    def update_classroom(classroom_id, new_data):
        classroom = Classroom.query.get(classroom_id)
        if not classroom:
            raise ClassroomNotFound
        classroom.name = new_data['name']
        db.session.commit()

    @staticmethod
    def delete_classroom(classroom_id):
        classroom = Classroom.query.get(classroom_id)
        if not classroom:
            raise ClassroomNotFound
        db.session.delete(classroom)
        db.session.commit()

class ClassroomNotFound(Exception):
        pass