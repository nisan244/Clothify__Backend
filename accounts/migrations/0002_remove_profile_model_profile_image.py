# Generated by Django 5.1.3 on 2025-01-01 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_model',
            name='profile_image',
        ),
    ]
