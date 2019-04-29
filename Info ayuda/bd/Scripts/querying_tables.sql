select * from barberos where dirbarbero = 'Callao' or dirbarbero = 'Ate'
select * from barberos where apebarbero like 'p%' and nombarbero = 'Carlos'
select * from clientes where estado = '0' order by apecliente desc
select count(*) from clientes where estado = '0' and dircliente = 'San Juan'

select s.desservicio, count(*) from reservas r inner join servicios s 
on r.codservicio=s.codservicio group by s.desservicio

select concat(b.nombarbero, b.apebarbero) Barbero,count(*) Cantidad from barberos b inner join 
reservas r on b.codbarbero=r.codbarbero
group by nombarbero order by b.apebarbero

select concat(b.nombarbero, b.apebarbero) Barbero,count(*) Cantidad, sum(s.costo) Costo from barberos b inner join 
reservas r on b.codbarbero=r.codbarbero
inner join servicios s on r.codservicio=s.codservicio
group by nombarbero order by sum(s.costo) desc

select * from reservas where fechaservicio >='2019-04-19'
select * from reservas where fechaservicio between '2019-04-19' and '2019-04-21'
select * from reservas where month(fechaservicio) = '05' and year(fechaservicio)='2019'
select * from reservas where month(fechaservicio) = '05' and year(fechaservicio)='2019' and day(fechaservicio)='14'
select * from reservas where observacion not like '%App%'
select * from reservas where observacion = ''
