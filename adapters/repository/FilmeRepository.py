from sqlalchemy.orm import Session
from core.models.Filme import Filme

class FilmeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        try:
            return self.db.query(Filme).all()
        except Exception as e:
            raise Exception(f"Não foi possível Buscar Filmes: {str(e)}")

    def get_by_id(self, filme_id):
        try:
            return self.db.query(Filme).filter_by(id=filme_id).first()
        except Exception as e:
            raise Exception(f"Não foi possível encontrar Filme: {str(e)}")

    def get_by_name(self, name):
        try:
            return self.db.query(Filme).filter_by(nome=name).first()
        except Exception as e:
            raise Exception(f"Não for encontrar Filme: {str(e)}")

    def get_by_genero(self, genero):
        try:
            return self.db.query(Filme).filter_by(genero=genero)
        except Exception as e:
            raise Exception(f"Não for encontrar genero: {str(e)}")

    def save(self, filme : Filme):
        try:
            self.db.add(filme)
            self.db.commit()
            return self.db.query(Filme).filter_by(nome=filme.nome, sinopse=filme.sinopse).first()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Erro ao criar o filme: {str(e)}")
