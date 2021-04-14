# Generated by Django 3.1.7 on 2021-04-14 08:12

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2021, 4, 14))]),
        ),
    ]