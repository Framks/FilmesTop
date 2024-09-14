from flask import Flask
from flask_migrate import Migrate
from infrastructure.db import db
from adapters.controllers.FilmeController import filme
from adapters.controllers.UserController import usuario
from adapters.controllers.AluguelController import Aluguel
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(filme)
    app.register_blueprint(usuario)
    app.register_blueprint(Aluguel)
    print(app.url_map)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

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