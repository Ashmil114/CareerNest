# Generated by Django 5.0.3 on 2024-03-15 16:46

import Staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_remove_jobsmodel_qualifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsmodel',
            name='qualifications',
            field=models.JSONField(default=Staff.models.default_qualifications),
        ),
    ]
