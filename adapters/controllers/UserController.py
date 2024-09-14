from flask import Blueprint, jsonify

from infrastructure.db import get_db
from core.services.UserService import UserService
from adapters.repository.UserRepository import UserRepository

usuario = Blueprint('usuario', __name__)

db = get_db()
repository = UserRepository(db.session)
usuario_service = UserService(repository=repository)

@usuario.route('/usuario/<int:id_user>', methods=["GET"])
def get_usuario_by_id(id_user):
    user = usuario_service.get_by_id(id_user)
    return jsonify(user)


