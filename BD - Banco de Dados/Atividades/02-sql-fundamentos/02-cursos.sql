CREATE DATABASE ayuka_silva_20260611;
USE ayuka_silva_20260611;

CREATE TABLE curso (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    nome    VARCHAR(100) NOT NULL
);

CREATE TABLE aluno (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    curso_id    INT,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
);

INSERT INTO curso (nome) VALUES ('Informática para Internet');
INSERT INTO curso (nome) VALUES ('Nutrição');
INSERT INTO curso (nome) VALUES ('Administração');

INSERT INTO aluno (nome, curso_id) VALUES ('Willian', 1);
INSERT INTO aluno (nome, curso_id) VALUES ('Yasmin', 1);
INSERT INTO aluno (nome, curso_id) VALUES ('Chris', 2);
INSERT INTO aluno (nome, curso_id) VALUES ('Mih', NULL);

INSERT INTO aluno (nome, curso_id) VALUES ('Mih', 99);

-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`ayuka_silva_20260611`.`aluno`, CONSTRAINT `aluno_ibfk_1` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`))

SELECT  a.nome, c.nome
FROM    aluno a
INNER JOIN curso c ON a.curso_id = c.id;

SELECT  a.nome, c.nome
FROM    curso c
LEFT JOIN aluno a ON c.id = a.curso_id;

SELECT  c.nome, a.nome
FROM    curso c
LEFT JOIN aluno a ON a.curso_id = c.id
WHERE   a.curso_id IS NULL;

SELECT  a.nome, c.nome
FROM    curso c
RIGHT JOIN aluno a ON c.id = a.curso_id;

DROP TABLE aluno;
DROP TABLE curso;
DROP DATABASE ayuka_silva_20260611;