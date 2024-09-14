from adapters.repository.FilmeRepository import FilmeRepository

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
            print(id)
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

    def criar(self, professor):
        try:
            self.repo.save(professor)
            filme = self.repo.get_by_id(professor.id).to_dict()
            return filme.to_dict()
        except Exception as e:
            raise Exception("Erro ao criar filme: " + str(e))