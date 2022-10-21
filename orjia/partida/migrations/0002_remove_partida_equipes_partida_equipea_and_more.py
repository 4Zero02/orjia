# Generated by Django 4.1 on 2022-10-21 20:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atletica', '0002_initial'),
        ('campanha', '0002_alter_competicao_campanha'),
        ('partida', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='equipes',
        ),
        migrations.AddField(
            model_name='partida',
            name='equipeA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Equipe_partida_A', to='atletica.equipe'),
        ),
        migrations.AddField(
            model_name='partida',
            name='equipeB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Equipe_partida_B', to='atletica.equipe'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='competicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='campanha.competicao'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='data',
            field=models.DateField(default=datetime.date.today, verbose_name='Data da partida'),
        ),
    ]
