import pytest
from unittest.mock import Mock
from core.models.Aluguel import Aluguel
from core.models.Filme import Filme
from core.models.Usuario import Usuario
from datetime import datetime
from core.services.AluguelService import AluguelService

mock_aluguel_repo = Mock()
mock_usuario_repo = Mock()
mock_filme_repo = Mock()
service = AluguelService(mock_aluguel_repo, mock_usuario_repo, mock_filme_repo)

def test_alugar_sucesso():
    mock_usuario_repo.get_by_id.return_value = Usuario(
        id=1,
        nome="João da Silva",
        email="joao.silva@example.com",
        celular="123456789"
    )
    mock_filme_repo.get_by_id.return_value = Filme(
        id=1,
        nome="Marfia 1",
        genero="Ação",
        ano=2024,
        sinopse="Uma sinopse fictícia.",
        diretor="Diretor Fictício"
    )

    mock_aluguel_repo.get_aluguel.return_value = None
    mock_aluguel_repo.save.return_value = Aluguel(id=1,nota=None,data_aluguel=datetime.now(),usuario_id=1,filme_id=1, filme=Filme(
        id=1,
        nome="Marfia 1",
        genero="Ação",
        ano=2024,
        sinopse="Uma sinopse fictícia.",
        diretor="Diretor Fictício"
    ), usuario=Usuario(
        id=1,
        nome="João da Silva",
        email="joao.silva@example.com",
        celular="123456789"
    ) )


    response = service.alugar(1, 1)

    mock_aluguel_repo.save.assert_called_once()

def test_alugar_filme_ja_alugado():
    mock_usuario_repo.get_by_id.return_value = Filme(
        nome="Marfia 1",
        genero="Ação",
        ano=2024,
        sinopse="Uma sinopse fictícia.",
        diretor="Diretor Fictício"
    )
    mock_filme_repo.get_by_id.return_value = Usuario(
        nome="João da Silva",
        email="joao.silva@example.com",
        celular="123456789"
    )
    mock_aluguel_repo.get_aluguel.return_value = Aluguel(usuario_id=1, filme_id=1, data_aluguel=datetime.now(), nota=9)

    response= service.alugar(1, 1)

    assert response is None

def test_alugar_usuario_nao_encontrado():

    mock_usuario_repo.get_by_id.return_value = None

    response = service.alugar(1, 1)

    assert response is None

def test_atribuir_nota_sucesso():
    mock_usuario_repo.get_by_id.return_value = Filme(
        nome="Marfia 1",
        genero="Ação",
        ano=2024,
        sinopse="Uma sinopse fictícia.",
        diretor="Diretor Fictício"
    )
    mock_filme_repo.get_by_id.return_value = Usuario(
        nome="João da Silva",
        email="joao.silva@example.com",
        celular="123456789"
    )
    mock_aluguel_repo.get_aluguel.return_value = Aluguel(usuario_id=1, filme_id=1, data_aluguel=datetime.now())

    response, status_code = service.atribuir_nota(1, 1, 8)

    assert status_code == 200
    assert response["message"] == "Nota atribuída com sucesso"
    assert response["nota"] == 8

def test_atribuir_nota_invalida():

    response= service.atribuir_nota(1, 1, 11)

    assert response is None
