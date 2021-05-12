# Generated by Django 3.1.7 on 2021-05-10 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0009_auto_20210510_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='attempts_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]