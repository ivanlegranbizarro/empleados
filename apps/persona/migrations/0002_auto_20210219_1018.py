# Generated by Django 3.1.6 on 2021-02-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidades', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Habilidades de nuestros empleados',
                'verbose_name_plural': 'Habilidades de nuestros empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado', verbose_name='Avatar'),
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'last_name')},
        ),
    ]