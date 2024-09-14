from infrastructure.db import db

class Aluguel(db.Model):
    __tablename__ = 'aluguel'

    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer)
    data_aluguel = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    filme_id = db.Column(db.Integer, db.ForeignKey('filme.id'), nullable=False)

    usuario = db.relationship('Usuario', backref='alugueis')
    filme = db.relationship('Filme', backref='alugueis')
