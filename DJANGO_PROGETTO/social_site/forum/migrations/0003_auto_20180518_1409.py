# Generated by Django 2.0.5 on 2018-05-18 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180518_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussione',
            name='sezione_appartenenza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Sezione'),
        ),
    ]
