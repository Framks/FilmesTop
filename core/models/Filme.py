from infrastructure.db import db


class Filme(db.Model):
    __tablename__ = 'filme'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    genero = db.Column(db.String)
    ano = db.Column(db.Integer)
    sinopse = db.Column(db.String)
    diretor = db.Column(db.String)

    def to_dict(self):
        return {
            "id":self.id,
            "nome": self.nome,
            "genero": self.genero,
            "ano":self.ano,
            "sinopse":self.sinopse,
            "diretor":self.diretor
        }