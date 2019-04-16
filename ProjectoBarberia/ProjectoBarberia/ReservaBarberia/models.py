from django.db import models

# Create your models here.

class Barbero(models.Model):
    codbarbero = models.AutoField(primary_key = True) #autoincremento y es una llave primaria
    barberonom = models.CharField(max_length = 150, blank = False, null = False)
    fecharegistro = models.DateField()
    description = models.TextField()
    correo = models.EmailField(max_length=255)

    class Meta:
        verbose_name = 'Barbero'
        verbose_name_plural = 'Barberos'
        ordering = ['barberonom']

    def __str__(self):
        return self.barberonom

class Cliente(models.Model):
    codcliente = models.AutoField('Codigo',primary_key = True) #autoincremento y es una llave primaria
    clientenom = models.CharField('Cliente',max_length = 150, blank = False, null = False)
    telefono = models.CharField('Telefono',max_length = 12)
    fecharegistro = models.DateField('Fecha')
    correo = models.EmailField('Correo',max_length=255)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['clientenom']

    def __str__(self):
        return self.clientenom

class Servicio(models.Model):
    codser = models.AutoField('Codigo',primary_key = True) #autoincremento y es una llave primaria
    servicio = models.CharField('Servicio',max_length = 150, blank = False, null = False)
    nomcorto = models.CharField('Abreviatura',max_length = 50, blank = False, null = False)
    fecharegistro = models.DateField('Fecha')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nomcorto']

    def __str__(self):
        return self.servicio

class Reserva(models.Model):
    codreserva = models.AutoField(primary_key = True)
    codbarbero = models.ForeignKey(Barbero,on_delete = models.CASCADE)
    codclie = models.ForeignKey(Cliente,on_delete = models.CASCADE)
    codserv = models.ManyToManyField(Servicio)
    fecha = models.DateField() #por defecto retorna la fecha del sistema
    obs = models.TextField()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['fecha']


