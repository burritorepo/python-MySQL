CREATE TABLE tbl_barberos (
cod_barbero varchar(9) primary key,
cod_espec int,
nom_barbero varchar(100),
ape_barbero varchar(100),
usu_crea int,
fecha_crea datetime)


CREATE TABLE tbl_especialidad (
cod_espec int primary key,
nom_espec varchar(50) NOT NULL)

CREATE TABLE tbl_barberos (
cod_barbero varchar(9) primary key,
cod_espec int,
nom_barbero varchar(100),
ape_barbero varchar(100),
usu_crea int,
fecha_crea datetime)

CREATE TABLE tbl_bar_esp (
cod_bar_esp int primary key,
cod_barbero varchar(9), FOREIGN KEY (cod_barbero) REFERENCES tbl_barberos (cod_barbero),
cod_espec int, FOREIGN KEY (cod_espec) REFERENCES tbl_especialidad (cod_espec))