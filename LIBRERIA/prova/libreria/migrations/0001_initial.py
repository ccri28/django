# Generated by Django 2.0.5 on 2018-05-20 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('nazione', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Autore',
                'verbose_name_plural': 'Autori',
            },
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Genere',
                'verbose_name_plural': 'Generi',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.Autore')),
                ('genere', models.ManyToManyField(to='libreria.Genere')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libri',
            },
        ),
    ]