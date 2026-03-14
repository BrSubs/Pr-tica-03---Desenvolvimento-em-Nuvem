CREATE DATABASE IF NOT EXISTS projeto_db;
USE projeto_db;

CREATE TABLE IF NOT EXISTS itens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cor VARCHAR(50)
);

INSERT INTO itens (nome, categoria) VALUES 
('Caderno', 'Vermelho'),
('Estojo Escolar', 'Cinza'),
('Caixa de lápis de cor', 'Multicolor');