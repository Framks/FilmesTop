from flask import Blueprint, jsonify , request

from core.services.UserService import UserService

def create_usuario_blueprint(cache, usuario_service: UserService):
    usuario = Blueprint('usuario', __name__)



    @usuario.route('/usuario/<int:id_user>', methods=["GET"])
    @cache.cached(timeout=300, key_prefix='usuario_by_id')
    def get_usuario_by_id(id_user):
        user = usuario_service.get_by_id(id_user)
        if user is None:
            return jsonify({'error': 'User not found'}),404
        return jsonify(user)

    @usuario.route('/usuario/', methods=["POST"])
    def create_usuario():
        usuario = request.json
        criado = usuario_service.criar(usuario)
        if criado is None:
            return jsonify({'error': 'User not created'}),404
        return jsonify(criado)

    return usuario