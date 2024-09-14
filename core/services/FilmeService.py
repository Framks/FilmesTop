from adapters.repository.FilmeRepository import FilmeRepository
from core.models.Filme import Filme


class FilmeService:
    def __init__(self, repo: FilmeRepository):
        self.repo = repo

    def get_all(self):
        try:
            filmes = []
            for film in self.repo.get_all():
                filmes.append(film.to_dict())
            return filmes
        except Exception as e:
            raise Exception("Erro ao buscar filmes: " + str(e))


    def get_by_id(self, id):
        try:
            filme = self.repo.get_by_id(id)
            return filme.to_dict()
        except Exception as e:
            raise Exception("Erro ao buscar filme: " + str(e))


    def get_by_genero(self, genero):
        try:
            filmes = []
            for film in self.repo.get_by_genero(genero):
                filmes.append(film.to_dict())
            return filmes
        except Exception as e:
            raise Exception("Erro ao buscar filmes por genero: " + str(e))

    def criar(self, filme):
        try:
            novo = Filme(nome=filme['nome'], genero=filme['genero'],sinopse=filme['sinopse'], ano=filme['ano'],diretor=filme['diretor'])
            filme_create = self.repo.save(novo)
            return filme_create.to_dict()
        except Exception as e:
            raise Exception("Erro ao criar filme: " + str(e))