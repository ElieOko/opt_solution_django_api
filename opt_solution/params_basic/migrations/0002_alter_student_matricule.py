# Generated by Django 5.0.6 on 2024-05-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matricule',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
