CREATE DATABASE ayuka_silva_20260618;
USE ayuka_silva_20260618;
CREATE TABLE livro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    autor VARCHAR(100),
    categoria VARCHAR(100),
    preco DECIMAL(10, 2),
    data_publicacao DATE
);
INSERT INTO livro (titulo, autor, categoria, preco, data_publicacao)
VALUES (
        '  Duna  ',
        'Frank Hebert',
        'Ficção Científica',
        72.13,
        '2017-04-28'
    ),
    (
        'Messias de Duna',
        'Frank Hebert',
        'Ficção Científica',
        66.40,
        '2017-07-05'
    ),
    (
        'Filhos de Duna',
        NULL,
        'Ficção Científica',
        65.26,
        '2017-08-31'
    ),
    (
        'O cara que estou afim não é um cara Vol.1',
        'Sumiko Arai',
        'Mangá',
        27.99,
        '2024-06-20'
    ),
    (
        'Little Witch Academia Vol.1',
        'Trigger',
        'Mangá',
        29.83,
        '2025-05-14'
    );
SELECT CONCAT(titulo, ' <', autor, '>') AS ficha
FROM livro;
SELECT UPPER(titulo) AS maiusculo
FROM livro;
SELECT CONCAT('[', titulo, ']') AS sem_trim,
    CONCAT('[', TRIM(titulo), ']') AS com_trim
FROM livro;
SELECT titulo,
    DATE_FORMAT(data_publicacao, '%d/%m/%Y') AS publicacao
FROM livro;
SELECT titulo,
    DATEDIFF(NOW(), data_publicacao) AS dias_publicado
FROM livro;
SELECT titulo,
    preco,
    ROUND(preco, 0) AS arredondado
FROM livro;
SELECT titulo,
    preco,
    CASE
        WHEN preco < 50 THEN 'Barato'
        WHEN preco < 100 THEN 'Médio'
        ELSE 'Caro'
    END AS classificacao
FROM livro;
SELECT titulo,
    COALESCE(autor, 'Autor desconhecido') AS autor
FROM livro;
SELECT COUNT(*) AS total_livros
FROM livro;
SELECT SUM(preco) AS preco_total,
    AVG(preco) AS media_preco
FROM livro;
SELECT MIN(preco) AS menor,
    MAX(preco) AS maior
FROM livro;
SELECT categoria,
    COUNT(*) AS qtd,
    AVG(preco) AS media
FROM livro
GROUP BY categoria;
SELECT categoria,
    COUNT(*) AS qtd
FROM livro
GROUP BY categoria
HAVING COUNT(*) > 1;
DROP TABLE livro;
DROP DATABASE ayuka_silva_20260618;