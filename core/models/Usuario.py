from infrastructure.db import db


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    celular = db.Column(db.String)

    def to_disct(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'celular': self.celular
        }