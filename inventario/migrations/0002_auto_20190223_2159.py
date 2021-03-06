# Generated by Django 2.1.5 on 2019-02-23 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='coleccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Coleccion'),
        ),
    ]
