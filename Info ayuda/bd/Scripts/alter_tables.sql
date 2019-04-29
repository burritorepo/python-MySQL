show databases
show tables
describe barberos
rename table barberos to barbero_2

alter table barberos add fechacreacion date
alter table barberos add codusuario int
alter table barberos add ejemplo varchar(2)
alter table barberos drop column ejemplo
alter table barberos change fechacreacion fecha_cre date
alter table barberos modify column fecha_cre date
