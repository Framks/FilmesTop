from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from core.models.Aluguel import Aluguel


class AluguelRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_by_user_id(self, user_id):
        try:
            return self.db_session.query(Aluguel).filter_by(usuario_id=user_id).all()
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar aluguéis do usuário: {str(e)}")

    def get_aluguel(self, id_usuario, id_filme):
        try:
            return self.db_session.query(Aluguel).filter_by(usuario_id=id_usuario, filme_id=id_filme).first()
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar o aluguel: {str(e)}")

    def save(self, aluguel: Aluguel):
        try:
            existing_aluguel = self.db_session.query(Aluguel).filter_by(usuario_id=aluguel.usuario_id, filme_id=aluguel.filme_id).first()
            if existing_aluguel:
                existing_aluguel.nota = aluguel.nota
                existing_aluguel.data_aluguel = aluguel.data_aluguel
            else:
                self.db_session.add(aluguel)
            self.db_session.commit()
            return aluguel

        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Erro ao salvar aluguel: {str(e)}")