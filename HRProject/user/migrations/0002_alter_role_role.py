# Generated by Django 4.2.7 on 2024-05-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(default='hr', max_length=100),
        ),
    ]
