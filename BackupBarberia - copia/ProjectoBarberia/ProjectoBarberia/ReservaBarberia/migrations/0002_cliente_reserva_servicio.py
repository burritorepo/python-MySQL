# Generated by Django 2.2 on 2019-05-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservaBarberia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codcliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('clientenom', models.CharField(max_length=150, verbose_name='Cliente')),
                ('telefono', models.CharField(max_length=12, verbose_name='Telefono')),
                ('fecharegistro', models.DateField(verbose_name='Fecha')),
                ('correo', models.EmailField(max_length=255, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['clientenom'],
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('codser', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('servicio', models.CharField(max_length=150, verbose_name='Servicio')),
                ('nomcorto', models.CharField(max_length=50, verbose_name='Abreviatura')),
                ('fecharegistro', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['nomcorto'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codreserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('obs', models.TextField()),
                ('codbarbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaBarberia.Barbero')),
                ('codclie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaBarberia.Cliente')),
                ('codserv', models.ManyToManyField(to='ReservaBarberia.Servicio')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['fecha'],
            },
        ),
    ]
