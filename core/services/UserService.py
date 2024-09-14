from adapters.repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_by_id(self, id_user):
        try:
            usuario = self.repository.get_by_id(id_user)
            return usuario.to_disct()
        except Exception as e:
            raise e