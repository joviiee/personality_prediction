# Generated by Django 5.0 on 2024-01-21 18:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_questions_delete_geeksmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='index',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
