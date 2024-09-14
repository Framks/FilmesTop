from flask import Blueprint, jsonify

from core.services.FilmeService import FilmeService
from adapters.repository.FilmeRepository import FilmeRepository
from infrastructure.db import get_db

filme = Blueprint('filme', __name__)

db = get_db()
repository = FilmeRepository(db.session)
filme_service = FilmeService(repo=repository)

@filme.route('/filme/', methods=['GET'])
def get_all_filme():
    filmes = filme_service.get_all()
    return jsonify(filmes)

@filme.route('/filme/<int:filme_id>', methods=['GET'])
def get_filme_by_id(filme_id):
    filme = filme_service.get_by_id(id=filme_id)
    return jsonify(filme)

@filme.route('/filme/<string:filme_genero>', methods=['GET'])
def get_filme_by_gender(filme_genero):
    filmes = filme_service.get_by_genero(filme_genero)
    return jsonify(filmes)

