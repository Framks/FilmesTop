from flask import Blueprint, request, jsonify

from core.services.AluguelService import AluguelService
def create_aluguel_blueprint(cache, aluguel_service: AluguelService):
    aluguel_bp = Blueprint('aluguel', __name__)

    @aluguel_bp.route("/aluguel/usuario/<int:id_usuario>/alugar/<int:filme>", methods=["POST"])
    def alugar(id_usuario, filme):
        return jsonify(aluguel_service.alugar(id_usuario, filme))

    @aluguel_bp.route("/aluguel/usuario/<int:id>", methods=["GET"])
    @cache.cached(timeout=300, key_prefix='get_aluguel_usuario_by_id')
    def get_aluguel_by(id):
        return jsonify(aluguel_service.get_alugueis_by_id(id))

    @aluguel_bp.route("/aluguel/usuario/<int:id_usuario>/filme/<int:filme>", methods=["PUT"])
    def filme(id_usuario, filme):
        data = request.json
        nota = data.get("nota")
        return jsonify(aluguel_service.atribuir_nota(id_usuario, filme, nota))

    return aluguel_bp