# Generated by Django 5.1.3 on 2025-01-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='rating',
            field=models.CharField(choices=[('⭐', 1), ('⭐⭐', 2), ('⭐⭐⭐', 3), ('⭐⭐⭐⭐', 4), ('⭐⭐⭐⭐⭐', 5)], max_length=6),
        ),
    ]
