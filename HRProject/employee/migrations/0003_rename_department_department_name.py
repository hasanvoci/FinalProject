# Generated by Django 4.2.7 on 2024-05-19 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='name',
        ),
    ]
