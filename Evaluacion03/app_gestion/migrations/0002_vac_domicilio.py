# Generated by Django 4.0.5 on 2022-07-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vac_Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre_completo', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
