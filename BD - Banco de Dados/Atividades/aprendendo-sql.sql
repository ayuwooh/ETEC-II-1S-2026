CREATE DATABASE ayuka_henrique_20260528;

USE ayuka_henrique_20260528;

CREATE TABLE produto (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NOT NULL, preco DECIMAL(10,2), data_cadastro DATE);

DESCRIBE produto;

INSERT INTO produto (nome, preco, data_cadastro) VALUES ('Memória RAM', 409.99, '2026-05-28');
INSERT INTO produto (nome, preco, data_cadastro) VALUES ('Teclado', 659.90, '2026-05-28');
INSERT INTO produto (nome, preco, data_cadastro) VALUES ('Monitor', 899.99, '2026-05-28');

SELECT * FROM produto;

SELECT * FROM produto WHERE preco > 50 ORDER BY preco;

UPDATE produto SET preco = 949.99 WHERE id = 3;

SELECT * FROM produto WHERE id = 3;

ALTER TABLE produto ADD COLUMN quantidade_estoque INT;

UPDATE produto SET quantidade_estoque = 7 WHERE id = 1;

UPDATE produto SET quantidade_estoque = 14 WHERE id = 3;

UPDATE produto SET quantidade_estoque = 32 WHERE id = 2;

SELECT * FROM produto;

DELETE FROM produto WHERE id = 2;

SELECT * FROM produto;

-- DESAFIO OPCIONAL

SELECT nome, preco FROM produto WHERE nome LIKE 'M%';

-- 

DROP TABLE produto;

DROP DATABASE ayuka_henrique_20260528;