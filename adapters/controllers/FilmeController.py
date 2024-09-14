from flask import Blueprint, jsonify, request

from core.services.FilmeService import FilmeService

def create_filme_blueprint(cache, filme_service: FilmeService):
    filme = Blueprint('filme', __name__)

    @filme.route('/filme/', methods=['GET'])
    @cache.cached(timeout=300, key_prefix='get_all_filme')
    def get_all_filme():
        filmes = filme_service.get_all()
        if not filmes:
            return jsonify({'error': 'No filmes found'}), 404
        return jsonify(filmes)

    @filme.route('/filme/id/<int:id>', methods=['GET'])
    @cache.cached(timeout=300, key_prefix='get_filme_by_id')
    def get_filme_by_id(id):
        filme = filme_service.get_by_id(id=id)
        if filme is None:
            return jsonify({'error': 'Filme not found'}), 404
        return jsonify(filme)

    @filme.route('/filme/<string:filme_genero>', methods=['GET'])
    @cache.cached(timeout=300, key_prefix='get_filme_by_gender')
    def get_filme_by_gender(filme_genero):
        filmes = filme_service.get_by_genero(filme_genero)
        if not filmes:
            return jsonify({'error': 'No filmes found'}), 404
        return jsonify(filmes)

    @filme.route('/filme/', methods=['POST'])
    def create_filme():
        data = request.get_json()
        filme = filme_service.criar(data)
        if not filme:
            return jsonify({'error': 'No filme created'}), 404
        return jsonify(filme),201

    return filme