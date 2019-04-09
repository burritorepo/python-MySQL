# Generated by Django 2.2 on 2019-04-09 21:42

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('ReservaBarberia', '0002_cliente_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default=django.utils.timezone.now, max_length=12, verbose_name='Telefono'),
            preserve_default=False,
        ),
    ]