# Generated by Django 3.1.6 on 2021-02-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210218_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=1, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='subtitulo',
            field=models.CharField(max_length=100, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
