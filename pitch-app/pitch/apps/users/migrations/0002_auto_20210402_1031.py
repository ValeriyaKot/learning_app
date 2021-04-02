# Generated by Django 3.1.7 on 2021-04-02 10:31

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
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.datetime(2021, 4, 2, 10, 31, 37, 109486))]),
        ),
    ]
