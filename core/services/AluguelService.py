from datetime import datetime

from adapters.repository.FilmeRepository import FilmeRepository
from adapters.repository.AluguelRepository import AluguelRepository
from adapters.repository.UserRepository import UserRepository
from core.models.Aluguel import Aluguel


class AluguelService:
    def __init__(self, repository: AluguelRepository, usuario_repository: UserRepository, filme_repository: FilmeRepository):
        self.repository = repository
        self.usuario_repository = usuario_repository
        self.filme_repository = filme_repository

    def alugar(self, id_usuario, filme_id):
        try:
            usuario = self.usuario_repository.get_by_id(id_usuario)
            if not usuario:
                return {"message": "Usuário não encontrado"}, 404

            filme_obj = self.filme_repository.get_by_id(filme_id)
            if not filme_obj:
                return {"message": "Filme não encontrado"}, 404

            aluguel_existente = self.repository.get_aluguel(id_usuario, filme_obj.id)
            if aluguel_existente:
                return {"message": "Filme já alugado por este usuário"}, 409

            novo_aluguel = Aluguel(usuario_id=id_usuario, filme_id=filme_obj.id, data_aluguel=datetime.now())
            self.repository.save(novo_aluguel)
            return {"message": "Filme alugado com sucesso"}, 201

        except Exception as e:
            raise Exception("Erro ao alugar filme: " + str(e))



    def atribuir_nota(self, id_usuario, filme_id, nota):
        try:
            if nota < 0 or nota > 10:
                return {"message": "Nota inválida. Deve estar entre 0 e 10"}, 400
            usuario = self.usuario_repository.get_by_id(id_usuario)

            if not usuario:
                return {"message": "Usuário não encontrado"}, 404

            filme_obj = self.filme_repository.get_by_id(filme_id)
            if not filme_obj:
                return {"message": "Filme não encontrado"}, 404

            aluguel = self.repository.get_aluguel(id_usuario, filme_obj.id)
            if not aluguel:
                return {"message": "Usuário não alugou este filme"}, 404

            aluguel.nota = nota
            self.repository.save(aluguel)
            return {"message": "Nota atribuída com sucesso", "filme": filme_obj.nome, "nota": nota}, 200

        except Exception as e:
            raise Exception("Erro ao avaliar filmes: " + str(e))