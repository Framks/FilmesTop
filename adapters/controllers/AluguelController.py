from flask import Blueprint, request, jsonify

from adapters.repository.FilmeRepository import FilmeRepository
from adapters.repository.UserRepository import UserRepository
from core.services.AluguelService import AluguelService
from adapters.repository.AluguelRepository import AluguelRepository
from infrastructure.db import get_db

Aluguel = Blueprint('aluguel', __name__)

db = get_db()
alugel_repository = AluguelRepository(db.session)
filme_repository = FilmeRepository(db.session)
user_repository = UserRepository(db.session)
aluguel_service = AluguelService(repository=alugel_repository, filme_repository=filme_repository, usuario_repository=user_repository)

@Aluguel.route("/usuario/<int:id_usuario>/alugar/<int:filme>", methods=["POST"])
def alugar(id_usuario, filme):
    return jsonify(aluguel_service.alugar(id_usuario, filme))

@Aluguel.route("/usuario/<int:id_usuario>/filme/<int:filme>", methods=["PUT"])
def filme(id_usuario, filme):
    data = request.json
    nota = data.get("nota")
    return jsonify(aluguel_service.atribuir_nota(id_usuario, filme, nota))

