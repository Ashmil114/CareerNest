# Generated by Django 5.0.3 on 2024-03-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsmodel',
            name='experiance',
            field=models.FloatField(default=0),
        ),
    ]
