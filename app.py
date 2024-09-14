from flask import Flask
from flask_caching import Cache
from flask_migrate import Migrate

from infrastructure.db import db
from core.services.AluguelService import AluguelService
from core.services.UserService import UserService
from core.services.FilmeService import FilmeService
from adapters.repository.UserRepository import UserRepository
from adapters.repository.FilmeRepository import FilmeRepository
from adapters.controllers.FilmeController import create_filme_blueprint
from adapters.controllers.UserController import create_usuario_blueprint
from adapters.repository.AluguelRepository import AluguelRepository
from adapters.controllers.AluguelController import create_aluguel_blueprint
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    cache = Cache(app)
    migrate = Migrate(app, db)

    filme_repository = FilmeRepository(db.session)
    filme_service = FilmeService(repo=filme_repository)

    user_repository = UserRepository(db.session)
    usuario_service = UserService(repository=user_repository)

    alugel_repository = AluguelRepository(db.session)
    aluguel_service = AluguelService(repository=alugel_repository, filme_repository=filme_repository,
                                     usuario_repository=user_repository)

    app.register_blueprint(create_filme_blueprint(cache,filme_service))
    app.register_blueprint(create_usuario_blueprint(cache, usuario_service))
    app.register_blueprint(create_aluguel_blueprint(cache, aluguel_service))

    print(app.url_map)
    return app


if __name__ == '__main__':
    app = create_app()

    app.run()

# problema um onde fica a função de alugar filme
# em um service proprio do aluguel ou no usuario
# e o aluguel
# do arquivo
# 4. o usuário deve ser capaz de associar uma nota a cada filme já alugado;
# com isso eu decido que vai ter um novo arquivo para aluguel pois pode vim a ter outras regras de negocio
# referente o


## se um usuario alugar o mesmo filme duas vezes em datas diferentes como fica?
##
##