# Generated by Django 3.2.9 on 2022-01-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=150)),
                ('mostrar', models.BooleanField(default=True)),
                ('local', models.CharField(default='Campinas', max_length=30)),
                ('requisitos', models.CharField(max_length=100)),
                ('resposabilidades', models.CharField(max_length=100)),
                ('beneficios', models.CharField(max_length=100)),
            ],
        ),
    ]
