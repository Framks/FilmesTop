from sqlalchemy.orm import Session
from core.models.Usuario import Usuario


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        try:
            return self.db.query(Usuario).all()
        except Exception as e:
            raise Exception(f"Não foi possível Buscar Usuarios: {str(e)}")


    def get_by_id(self, user_id):
        try:
            return self.db.query(Usuario).filter_by(id=user_id).first()
        except Exception as e:
            raise Exception(f"Não foi possível encontrar usuario: {str(e)}")

    def save(self, usuario: Usuario):
        try:
            self.db.add(usuario)
            self.db.commit()
            return self.db.query(Usuario).filter_by(email=usuario.email,nome=usuario.nome).first()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Não foi possível criar o usuario: {str(e)}")