-- Cria a tabela Cliente
CREATE TABLE Cliente (
id_cliente INTEGER PRIMARY KEY auto_increment,
nome VARCHAR(50),
sobrenome VARCHAR(50),
cpf VARCHAR(20),
data_nascimento VARCHAR(50),
email VARCHAR(100),
senha VARCHAR(50),
telefone VARCHAR(20),
fk_Plano_Mensal_id_plano INTEGER
);

-- Cria a tabela Plano_Mensal
CREATE TABLE Plano_Mensal (
id_plano INTEGER PRIMARY KEY,
nome VARCHAR(50),
descricao VARCHAR(255),
preco DECIMAL(10,2)
);

-- Cria a tabela Forma_Pagamento
CREATE TABLE Forma_Pagamento (
id_forma_pagamento INTEGER PRIMARY KEY,
tipo_pagamento VARCHAR(50),
fk_Plano_Mensal_id_plano INTEGER
);

-- Cria a tabela Ficha_de_Treino
CREATE TABLE Ficha_de_Treino (
id_ficha INTEGER PRIMARY KEY auto_increment,
data_criacao VARCHAR(50),
descricao VARCHAR(255),
duracao_treino VARCHAR(50),
ombro_lateral VARCHAR(100),
ombro_frontal VARCHAR(100),
supino_reto VARCHAR(100),
supino_inclinado VARCHAR(100),
crucifixo VARCHAR(100),
puxador_frontal VARCHAR(100),
puxador_costas VARCHAR(100),
remada_baixa VARCHAR(100),
remada_cavalo VARCHAR(100),
triceps_corda VARCHAR(100),
triceps_pulley VARCHAR(100),
rosca_biceps VARCHAR(100),
rosca_martelo VARCHAR(100),
agachamento VARCHAR(100),
legpress VARCHAR(100),
cadeira_extensora VARCHAR(100),
cadeira_flexora VARCHAR(100),
panturrilhas VARCHAR(100),
cardio VARCHAR(100),
fitdance VARCHAR(100),
luta VARCHAR(100),
fk_Cliente_id_cliente INTEGER
);

-- Cria a tabela Instrutor
CREATE TABLE Instrutor (
id_instrutor INTEGER PRIMARY KEY auto_increment,
nome VARCHAR(50),
sobrenome VARCHAR(50),
cpf VARCHAR(20),
data_nascimento VARCHAR(50),
email VARCHAR(100),
senha VARCHAR(50),
telefone VARCHAR(20)
);

-- Cria a tabela Feito
CREATE TABLE Feito (
fk_Ficha_de_Treino_id_ficha INTEGER,
fk_Instrutor_id_instrutor INTEGER,
PRIMARY KEY (fk_Ficha_de_Treino_id_ficha, fk_Instrutor_id_instrutor)
);

-- Adiciona as restrições de chave estrangeira
ALTER TABLE Cliente ADD CONSTRAINT FK_Cliente_2
FOREIGN KEY (fk_Plano_Mensal_id_plano)
REFERENCES Plano_Mensal (id_plano)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE Forma_Pagamento ADD CONSTRAINT FK_Forma_Pagamento_2
FOREIGN KEY (fk_Plano_Mensal_id_plano)
REFERENCES Plano_Mensal (id_plano)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE Ficha_de_Treino ADD CONSTRAINT FK_Ficha_de_Treino_2
FOREIGN KEY (fk_Cliente_id_cliente)
REFERENCES Cliente (id_cliente)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE Feito ADD CONSTRAINT FK_Feito_1
FOREIGN KEY (fk_Ficha_de_Treino_id_ficha)
REFERENCES Ficha_de_Treino (id_ficha)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE Feito ADD CONSTRAINT FK_Feito_2
FOREIGN KEY (fk_Instrutor_id_instrutor)
REFERENCES Instrutor (id_instrutor)
ON DELETE RESTRICT
ON UPDATE CASCADE;

-- Insere alguns dados na tabela Cliente
INSERT INTO Cliente (nome, sobrenome, cpf, data_nascimento, email, senha, telefone, fk_Plano_Mensal_id_plano) VALUES
('Ana', 'Silva', '111.222.333-44', '1995-01-01', 'ana@gmail.com', '123', '19 91234-5678', 1),
('Bruno', 'Souza', '222.333.444-55', '1996-02-02', 'bruno@outlook.com', '321', '19 92345-6789', 2);

-- Insere alguns dados na tabela Plano_Mensal
INSERT INTO Plano_Mensal (id_plano, nome, descricao, preco) VALUES
(1, 'Básico', 'Acesso as aulas de musculação e cardio', 120.00),
(2, 'VIP', 'Acesso as aulas de musculção, cardio, fitdance e lutas', 260.00);

-- Insere alguns dados na tabela Forma_Pagamento
INSERT INTO Forma_Pagamento (id_forma_pagamento, tipo_pagamento, fk_Plano_Mensal_id_plano) VALUES
(1, 'Dinheiro', 1),
(2, 'Cartão de crédito', 1);

-- Insere alguns dados na tabela Ficha_de_Treino
INSERT INTO Ficha_de_Treino (data_criacao, descricao, duracao_treino, ombro_lateral, ombro_frontal, supino_reto, supino_inclinado, crucifixo, puxador_frontal, 
puxador_costas, remada_baixa, remada_cavalo, triceps_corda, triceps_pulley, rosca_biceps, rosca_martelo, agachamento, legpress, cadeira_extensora, cadeira_flexora, 
panturrilhas, cardio, fitdance, luta, fk_Cliente_id_cliente) VALUES
('2023-01-01', 'Treino para hipertrofia com ênfase nos glúteos', '1 mês', null, null, null, null, null, null, null, null, null, null, null, null, null, 
'Agachamento na barra guiada 4 séries x 10 rep', 'Legpress 45 unilateral 4 séries x 12 rep', null, '4 séreies x 15 rep', '4 séries x 12 rep', null, null, 
null, 1),
('2023-02-12', 'Treino para hipertrofia e perda de peso', '1 mês', '4 séries x 10 rep', '4 séries x 10 rep', 'Supino com barra 4 séries x 8 rep', 'Supino com halteres 4 séries x 8 rep', 
'Crucifixo com halteres 4 séries x 8 rep', 'Puxada com barra triângulo 4 séries x 10 rep', '4 séries x 10 rep', 'Remada unilateral com halteres 4 séries x 8 rep', '4 séries x 8 rep', 
'4 séries x 12 rep', '4 séries até falha', 'Rosca barra W 4 séries x 10 rep', 'Rosca martelo unilateral 4 séries x 10 rep', 'Agachamento na barra livre 4 séries x 10 rep', 
'Legpress 90 4 séries x 10 rep', 'Cadeira unilateral 4 séries x 15 rep', '4 séreies x 15 rep', '4 séries x 12 rep', '20 minutos esteira pós musculação', null, 
null, 2);

-- Insere alguns dados na tabela Instrutor
INSERT INTO Instrutor (nome, sobrenome, cpf, data_nascimento, email, telefone) VALUES
('Rafael', 'Pereira', '567.890.123-45', '1990-08-19', 'rafael@gmail.com', '19 95555-5555'),
('Fernanda', 'Godoy', '678.901.234-56', '1995-06-20', 'fernanda@outlook.com', '19 96666-6666'),
('Gabriel', 'Santos', '789.012.345-67', '1994-07-07', 'gabriel@yahoo.com', '19 97777-7777');

-- Insere alguns dados na tabela Feito
INSERT INTO Feito (fk_Ficha_de_Treino_id_ficha, fk_Instrutor_id_instrutor) VALUES
(1, '3'),
(2, '1');

SELECT * FROM Ficha_de_Treino