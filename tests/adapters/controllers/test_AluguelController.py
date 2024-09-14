from app import create_app

def test_alugar_filme():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@localhost:5432/films-top",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })
    client = app.test_client()
    response = client.post("/aluguel/usuario/5/alugar/3")

    assert response.status_code == 200

def test_atribuir_nota_filme():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@localhost:5432/films-top",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    app.test_client().post("/aluguel/usuario/2/alugar/3")
    client = app.test_client()
    response = client.put("/aluguel/usuario/2/filme/3", json={"nota": 8})
    assert response.status_code == 200