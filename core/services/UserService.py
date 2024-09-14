from adapters.repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_by_id(self, id_user):
        try:
            usuario = self.repository.get_by_id(id_user)
            return usuario.to_disct()
        except Exception as e:
            raise Exception(f"Não foi possivel buscar o usuario: {e}")

    def criar(self, usuario):
        try:
            criado = self.repository.save(usuario)
            return criado.to_disct()
        except Exception as e:
            raise Exception(f"Não foi possivel criar o usuario: {e}")