# RESOLUÇÃO DE CASE FilmesTop

## Exectando o projeto:

Este projeto foi desenvolvido em Python e utiliza Docker para facilitar a criação de containers. Abaixo estão os pré-requisitos e os passos para configurar e rodar a aplicação.

### Pré-requisitos

Antes de executar o projeto, você precisará garantir que as seguintes ferramentas estão instaladas em sua máquina:

 - **Python(Versão 3.7 ou superior)**: [Instruções de instalação](https://www.python.org/downloads/)
 - **Docker**: [Instruções de instalação](https://docs.docker.com/get-docker/)
 - **Docker Compose**: [Instruções de instalação](https://docs.docker.com/compose/install/)
 - **Dependencias do projeto** (descritas no `requirements.txt`)

### Passos para Instalação

1. Clone o repositório do projeto:

    No terminal, execute o seguinte comando para clonar o repositório para sua máquina local:
    ```bash
    git clone https://github.com/Framks/FilmesTop.git
    ```
2. Instale as dependências:

    Navegue até o diretório do projeto clonado e instale as dependências usando o `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    Caso não tenha o pip instalado, você pode acessar o arquivo requirements.txt e instalar as dependências manualmente.

### Criando Containers Docker

Para configurar o ambiente do projeto usando Docker, siga as instruções abaixo:

1. Abra o diretório raiz do projeto no terminal.

2. Execute o comando a seguir para criar e iniciar os containers Docker:

    ```bash
    docker compose up 
    ```
   Isso configurará o ambiente com o banco de dados e o Redis para o Caching.

### Executando Testes na Aplicação

Após configurar o ambiente com Docker, você pode executar os testes para garantir que a aplicação está funcionando corretamente:

1. Defina o caminho do projeto com a variável de ambiente `PYTHONPATH`:

    ```bash
   export PYTHONPATH=.
    ```

2. No diretório raiz do projeto, execute os testes com o `pytest`:

    ```bash
    pytest
    ```

### Executando a Aplicação com Flask

Após configurar as dependências e rodar os testes, você pode iniciar a aplicação localmente utilizando o Flask:

1. No diretório raiz, execute o seguinte comando para iniciar o servidor Flask:

    ```bash
    flask run 
    ```
2. A aplicação estará disponível localmente no endereço http://127.0.0.1:5000/ por padrão.

### Tabela de endpoints

| Método HTTP | Endpoint                                               | Descrição                                      |
|-------------|---------------------------------------------------------|------------------------------------------------|
| GET         | `/filme/`                                               | Retorna todos os filmes.                       |
| GET         | `/filme/id/<id>`                                        | Retorna um filme por ID.                       |
| GET         | `/filme/<filme_genero>`                                 | Retorna filmes filtrados por gênero.           |
| POST        | `/filme/`                                               | Cria um novo filme.                            |
| GET         | `/usuario/<id_user>`                                    | Retorna um usuário por ID.                     |
| POST        | `/usuario/`                                             | Cria um novo usuário.                          |
| POST        | `/aluguel/usuario/<id_usuario>/alugar/<filme>`          | Aluga um filme para um usuário.                |
| GET         | `/aluguel/usuario/<id>`                                 | Retorna os aluguéis de um usuário por ID.      |
| PUT         | `/aluguel/usuario/<id_usuario>/filme/<filme>`           | Atribui uma nota a um filme alugado pelo usuário. |

### Detalhes dos Endpoints

1. **GET `/filme/`**  
   - Retorna uma lista com todos os filmes cadastrados no sistema.
   - saida:
   ```json
    [
      {
        "ano": 2014,
        "diretor": "Chad Stahelski",
        "genero": "Ação",
        "id": 2,
        "nome": "John Wick",
        "sinopse": "Um assassino aposentado busca vingança após a morte de seu cão."
      }
    ]
    ```
3. **GET `/filme/id/<id>`**  
   - Retorna as informações de um filme específico, identificado por seu ID.
   - saida:
   ```json
     {
       "ano": 2014,
       "diretor": "Chad Stahelski",
       "genero": "Ação",
       "id": 2,
       "nome": "John Wick",
       "sinopse": "Um assassino aposentado busca vingança após a morte de seu cão."
     }
   ```
4. **GET `/filme/<filme_genero>`**  
   - Filtra e retorna filmes com base no gênero informado.
   - saida:
   ```json
    [
      {
        "ano": 2014,
        "diretor": "Chad Stahelski",
        "genero": "Ação",
        "id": 2,
        "nome": "John Wick",
        "sinopse": "Um assassino aposentado busca vingança após a morte de seu cão."
      }
    ]
    ```
5. **POST `/filme/`**  
   - Cria um novo filme no sistema. O corpo da requisição deve conter as informações do filme.
   - Entrada:
   ```json
      {
        "nome":"nome",
        "genero":"genero",
        "ano":2000,
        "sinopse":"texto",
        "diretor":"diretor"
      }
   ```
6. **GET `/usuario/<id_user>`**  
   - Retorna as informações de um usuário específico com base no ID fornecido.
   - Saida
   ```json
      {
        "celular": "8888-8888",
        "email": "maria@gmail.com",
        "id": 2,
        "nome": "Maria Oliveira"
      }
    ```
7. **POST `/usuario/`**  
   - Cria um novo usuário no sistema. O corpo da requisição deve conter os dados do usuário.
   - Entrada:
   ```json
      {
        "nome": "nome",
        "celular": 88998765432,
        "email": "email@email.com"
      }  
    ```

8. **POST `/aluguel/usuario/<id_usuario>/alugar/<filme>`**  
   - Realiza o aluguel de um filme para o usuário identificado pelo ID.
   - Sem Entrada
   - Saida
   ```json
      null
    ```

9. **GET `/aluguel/usuario/<id>`**  
   - Retorna a lista de aluguéis realizados pelo usuário com o ID fornecido.
   - Saida:
   ````json
    [
      {
        "data_aluguel": "Sat, 14 Sep 2024 16:11:07 GMT",
        "id": 5,
        "nome_filme": "John Wick",
        "nota": null
      }
    ]
    ````

10. **PUT `/aluguel/usuario/<id_usuario>/filme/<filme>`**  
    - Atribui uma nota a um filme alugado pelo usuário. O corpo da requisição deve conter a nota.
    - Entrada
    ```json
    {
      "nota": 9
    }
    ```