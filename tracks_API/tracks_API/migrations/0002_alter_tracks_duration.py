# Generated by Django 4.0.5 on 2022-06-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='duration',
            field=models.FloatField(),
        ),
    ]