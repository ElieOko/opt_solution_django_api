# Generated by Django 5.0.6 on 2024-05-26 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params_basic', '0002_alter_student_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fk_promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='params_basic.promotion'),
        ),
    ]
