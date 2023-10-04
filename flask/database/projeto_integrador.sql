CREATE TABLE Plano_Mensal (
    id_plano INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(50),
    preco FLOAT
);

CREATE TABLE Forma_Pagamento (
    id_forma_pagamento INTEGER PRIMARY KEY,
    tipo_pagamento VARCHAR(50),
    fk_Plano_Mensal_id_plano INTEGER
);

CREATE TABLE Cliente (
	registro INTEGER auto_increment,
    cpf INTEGER PRIMARY KEY,
    endereco VARCHAR(100),
    tefefone VARCHAR(50),
    nome VARCHAR(50),
    data_nascimento DATE,
    fk_Plano_Mensal_id_plano INTEGER
);

CREATE TABLE Ficha_de_Treino (
    id_ficha INTEGER PRIMARY KEY auto_increment,
    data_criacao DATE,
    descricao VARCHAR(50),
    duracao_treino VARCHAR(50),
    fk_Cliente_cpf INTEGER
);

CREATE TABLE Instrutor (
    id_instrutor INTEGER auto_increment,
    nome VARCHAR(50),
    cpf INTEGER PRIMARY KEY,
    data_nascimento DATE,
    endereco VARCHAR(100),
    telefone VARCHAR(50)
);

CREATE TABLE Feito (
    fk_Ficha_de_Treino_id_ficha INTEGER,
    fk_Instrutor_cpf INTEGER
);
 
ALTER TABLE Cliente ADD CONSTRAINT FK_Cliente_2
    FOREIGN KEY (fk_Plano_Mensal_id_plano)
    REFERENCES Plano_Mensal (id_plano)
    ON DELETE SET NULL;
 
ALTER TABLE Forma_Pagamento ADD CONSTRAINT FK_Forma_Pagamento_2
    FOREIGN KEY (fk_Plano_Mensal_id_plano)
    REFERENCES Plano_Mensal (id_plano)
    ON DELETE RESTRICT;
 
ALTER TABLE Ficha_de_Treino ADD CONSTRAINT FK_Ficha_de_Treino_2
    FOREIGN KEY (fk_Cliente_cpf)
    REFERENCES Cliente (cpf)
    ON DELETE RESTRICT;
 
ALTER TABLE Feito ADD CONSTRAINT FK_Feito_1
    FOREIGN KEY (fk_Ficha_de_Treino_id_ficha)
    REFERENCES Ficha_de_Treino (id_ficha)
    ON DELETE RESTRICT;
 
ALTER TABLE Feito ADD CONSTRAINT FK_Feito_2
    FOREIGN KEY (fk_Instrutor_cpf)
    REFERENCES Instrutor (cpf)
    ON DELETE RESTRICT;