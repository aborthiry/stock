# Generated by Django 2.1.5 on 2019-03-09 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_auto_20190309_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='tipoorden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.TipoOrden'),
        ),
    ]
