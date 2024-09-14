\c films-top

CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    celular VARCHAR(20),
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE filme (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    ano INT,
    sinopse TEXT,
    diretor VARCHAR(100)
);

CREATE TABLE aluguel (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuario(id),
    filme_id INT REFERENCES filme(id),
    data_aluguel TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nota INT
);


/* Usuarios para usar nos testes */
INSERT INTO usuario (nome, celular, email) VALUES ('João Silva', '9999-9999', 'joao@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Maria Oliveira', '8888-8888', 'maria@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Carlos Souza', '7777-7777', 'carlos@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Ana Costa', '6666-6666', 'ana@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Bruno Alves', '5555-5555', 'bruno@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Paula Lima', '4444-4444', 'paula@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Rafael Borges', '3333-3333', 'rafael@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Beatriz Martins', '2222-2222', 'beatriz@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Lucas Rocha', '1111-1111', 'lucas@gmail.com');
INSERT INTO usuario (nome, celular, email) VALUES ('Fernanda Pereira', '0000-0000', 'fernanda@gmail.com');

/* filmes do genero ação  */
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Mad Max: Estrada da Fúria', 'Ação', 2015, 'Em um mundo pós-apocalíptico, Max se une a Furiosa para fugir de um tirano e seu exército.', 'George Miller');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('John Wick', 'Ação', 2014, 'Um assassino aposentado busca vingança após a morte de seu cão.', 'Chad Stahelski');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Velozes e Furiosos 7', 'Ação', 2015, 'Dom Toretto e sua equipe enfrentam um assassino que busca vingança.', 'James Wan');

/* filmes do genero Drama  */
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('A Lista de Schindler', 'Drama', 1993, 'Durante a Segunda Guerra, um empresário alemão salva judeus do Holocausto.', 'Steven Spielberg');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('À Procura da Felicidade', 'Drama', 2006, 'Um homem luta para criar seu filho enquanto enfrenta a pobreza.', 'Gabriele Muccino');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Clube da Luta', 'Drama', 1999, 'Um homem insatisfeito cria um clube de luta clandestino para extravasar sua frustração.', 'David Fincher');


/* filmes do genero Comédia  */
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Se Beber, Não Case', 'Comédia', 2009, 'Três amigos perdem o noivo após uma noite de farra em Las Vegas.', 'Todd Phillips');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('A Proposta', 'Comédia', 2009, 'Uma executiva força seu assistente a casar com ela para evitar ser deportada.', 'Anne Fletcher');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Zumbilândia', 'Comédia', 2009, 'Sobreviventes de um apocalipse zumbi atravessam os EUA em busca de segurança.', 'Ruben Fleischer');

/* filmes do genero Ficção científica  */
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Interstellar', 'Ficção Científica', 2014, 'Exploradores viajam através de um buraco de minhoca em busca de um novo lar para a humanidade.', 'Christopher Nolan');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Blade Runner 2049', 'Ficção Científica', 2017, 'Um replicante descobre um segredo que pode mudar a sociedade.', 'Denis Villeneuve');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('O Exterminador do Futuro', 'Ficção Científica', 1984, 'Um cyborg do futuro é enviado para matar a mãe de um líder rebelde.', 'James Cameron');

/* filmes do genero Terror  */
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Invocação do Mal', 'Terror', 2013, 'Investigadores paranormais ajudam uma família assombrada por uma entidade malévola.', 'James Wan');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('O Exorcista', 'Terror', 1973, 'Uma jovem é possuída por um demônio, e sua mãe busca ajuda de padres.', 'William Friedkin');
INSERT INTO filme (nome, genero, ano, sinopse, diretor) VALUES ('Hereditário', 'Terror', 2018, 'Uma família começa a desvendar segredos perturbadores após a morte da matriarca.', 'Ari Aster');

INSERT INTO aluguel (usuario_id, filme_id, data_aluguel, nota)
VALUES (1, 2, '2024-06-13 15:30:00', 9);

