# Generated by Django 2.1.5 on 2019-02-23 23:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20190223_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]