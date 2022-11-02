# Generated by Django 4.1 on 2022-11-02 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('C', 'Coletiva'), ('V', 'Virtual'), ('M', 'Mesa')], max_length=1)),
                ('max_atletas', models.PositiveIntegerField()),
                ('min_atletas', models.PositiveIntegerField()),
                ('tipo_confronto', models.CharField(choices=[('0', 'Mata-mata'), ('1', 'Todos-x-todos')], max_length=1)),
                ('eh_misto', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
                'ordering': ['nome'],
            },
        ),
    ]
