create database proyecto_barberia

productoscreate table productos (
codprod int not null auto_increment,
nomprod varchar(150),
abreprod varchar(50),
fechaven date,
estado char(1),
codeusu int,
fechaalta date,
primary key (codprod));

select * from productos


INSERT INTO `bdcotizaciones`.`productos` (`nomprod`, `abreprod`, `fechaven`, `estado`, `codeusu`, `fechaalta`) VALUES ('Honeywell Granit 1911i', 'HG1911i', '2030-04-27', '1', '1', '2019-04-27');
INSERT INTO `bdcotizaciones`.`productos` (`nomprod`, `abreprod`, `fechaven`, `estado`, `codeusu`, `fechaalta`) VALUES ('Honeywell Granit 1980i', 'HG1980i', '2030-04-27', '1', '1', '2019-04-27');
INSERT INTO `bdcotizaciones`.`productos` (`nomprod`, `abreprod`, `fechaven`, `estado`, `codeusu`, `fechaalta`) VALUES ('Honeywell Granit 1981i', 'HG1981i', '2030-04-27', '1', '1', '2019-04-27');

create table servicios (
codservicio int not null auto_increment,
desservicio varchar(150),
nomcostoservicio varchar(45),
costo decimal(6,2),
estado char(1),
primary key (codservicio))

create table clientes (
codcliente int not null auto_increment,
nomcliente varchar(150),
apecliente varchar(150),
dircliente varchar(120),
tlfcliente varchar(20),
estado char(1),
primary key (codcliente))

create table reservas (
codreserva int not null auto_increment,
codcliente int,
codservicio int,
codbarbero int,
fechaservicio date,
observacion text,
primary key (codreserva),
foreign key (codcliente) references clientes(codcliente), 
foreign key (codbarbero) references barberos(codbarbero),
foreign key (codservicio) references servicios(codservicio))


