# Generated by Django 5.0.4 on 2024-04-27 14:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='vacationPromotion',
            field=models.CharField(choices=[('jour', 'Jour'), ('soir', 'Soir')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]