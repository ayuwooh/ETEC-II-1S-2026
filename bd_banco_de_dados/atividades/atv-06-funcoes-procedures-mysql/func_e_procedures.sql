CREATE DATABASE ayuka_silva_20260625;
USE ayuka_silva_20260625;
CREATE TABLE venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendedor VARCHAR(100),
    regiao VARCHAR(60),
    valor DECIMAL(10, 2)
);
INSERT INTO venda (vendedor, regiao, valor)
VALUES ('Erik', 'Sudoeste', 349.99),
    ('Alex', 'Sul', 249.99),
    ('Ana', 'Sudoeste', 599.99),
    ('Alessandro', 'Norte', 199.99),
    ('Carlos', 'Nordeste', 59.99);

DELIMITER $$
CREATE FUNCTION com_comissao(valor DECIMAL(10, 2)) RETURNS DECIMAL(12, 2) DETERMINISTIC BEGIN RETURN valor * 0.10;
END $$
DELIMITER ;

SELECT vendedor,
    valor,
    com_comissao(valor) AS comissao FROM venda;

DELIMITER $$
CREATE FUNCTION classifica_venda(valor DECIMAL(10, 2)) RETURNS VARCHAR(10) DETERMINISTIC BEGIN IF valor >= 1000 THEN RETURN 'Alta';
ELSEIF valor >= 500 THEN RETURN 'Média';
ELSE RETURN 'Baixa';
END IF;
END $$
DELIMITER ;

SELECT vendedor,
    valor,
    classifica_venda(valor) AS classificacao
FROM venda;

DELIMITER $$
CREATE PROCEDURE vendas_da_regiao(IN p_regiao VARCHAR(60)) BEGIN
SELECT id,
    vendedor,
    valor
FROM venda
WHERE regiao = p_regiao;
END $$
DELIMITER ;

CALL vendas_da_regiao('Sudoeste');

DELIMITER $$
CREATE PROCEDURE total_da_regiao(IN p_regiao VARCHAR(60), OUT total DECIMAL(10, 2)) BEGIN
SELECT SUM(valor) INTO total
FROM venda
WHERE regiao = p_regiao;
END $$
DELIMITER ;

CALL total_da_regiao('Sudoeste', @qtd);
SELECT @qtd AS total_em_sudoeste;

SHOW FUNCTION STATUS
WHERE Db = 'ayuka_silva_20260625';

SHOW PROCEDURE STATUS
WHERE Db = 'ayuka_silva_20260625';

DROP FUNCTION IF EXISTS com_comissao;
DROP FUNCTION IF EXISTS classifica_venda;
DROP PROCEDURE IF EXISTS vendas_da_regiao;
DROP PROCEDURE IF EXISTS contar_por_regiao;
DROP PROCEDURE IF EXISTS total_da_regiao;
DROP TABLE venda;
DROP DATABASE ayuka_silva_20260625;