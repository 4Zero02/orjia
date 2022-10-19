# Generated by Django 4.1 on 2022-10-19 20:33

import atletica.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletica', '0003_equipe_competicao_alter_atleta_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['pontos'], 'verbose_name': 'Pontuação', 'verbose_name_plural': 'Pontuação'},
        ),
        migrations.AddField(
            model_name='atletica',
            name='logo',
            field=models.ImageField(null=True, upload_to=atletica.models.upload_photo),
        ),
    ]
