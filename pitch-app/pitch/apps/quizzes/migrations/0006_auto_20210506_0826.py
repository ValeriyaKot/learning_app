# Generated by Django 3.1.7 on 2021-05-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_auto_20210505_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='attempts_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
