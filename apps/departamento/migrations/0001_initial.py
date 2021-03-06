# Generated by Django 3.1.6 on 2021-02-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, verbose_name='Abreviatura')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
    ]
