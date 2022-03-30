create table client (
		nif varchar(9) primary key,
        dataregistre timestamp,
        nom varchar(20),
        cognom1 varchar(30),
        cognom2 varchar(30),
        address varchar(50),
        provincia varchar(2),
        poblacio varchar(3),
        telefon INT
        email varchar(30),
        datanaixement date,
        );

create table historial (
    id bigint primary key AUTO_INCREMENT,
    nif varchar(9),
    data date,
    hora time
    motiu varchar(140)
    tipus(enum('entrada','sortida'))
    serveis INT
    preu decimal(8,2),
    FOREIGN KEY (nif) REFERENCES client(nif)
    );
    );

create table reserves (
    nif varchar(9) primary key,
    data date,
    hora time,
    motiu varchar(140),
    datares bigint,
    FOREIGN KEY (nif) REFERENCES client(nif)
    );
    );

create table poblacio (
    idpro varchar(2),
    id varchar(3),
    control varchar(1),
    nom varchar(50)
    );

create table provincia (
    id varchar(2),
    nom varchar(50),
    );

create table detall(
    id bigint primary key,
    nif varchar(9),
    servei INT
    );

create table festius (
    data_in date,
    data_fi date,
    descripcio varchar(60)
    );

create table servei(
    id INT primary key,
    nom varchar(30),
    detall varchar(120),
    preu decimal(8,2)
    );
