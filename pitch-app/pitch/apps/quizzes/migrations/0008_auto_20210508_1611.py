# Generated by Django 3.1.7 on 2021-05-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_auto_20210508_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
