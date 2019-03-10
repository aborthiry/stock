# Generated by Django 2.1.5 on 2019-03-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_auto_20190309_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='tipodeorden',
            field=models.CharField(choices=[('1', 'Salida - Venta'), ('2', 'Salida - Distribución'), ('3', 'Salida - Donación'), ('4', 'Entrada - Impresión'), ('5', 'Entrada - Distribución')], default='1', max_length=1),
        ),
    ]
