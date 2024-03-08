# Generated by Django 5.0.3 on 2024-03-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('remote', 'remote'), ('parttime', 'parttime'), ('office', 'office')], max_length=100)),
                ('vaccancies', models.IntegerField()),
                ('package', models.CharField(max_length=100)),
                ('requirements', models.TextField(max_length=500)),
            ],
        ),
    ]
