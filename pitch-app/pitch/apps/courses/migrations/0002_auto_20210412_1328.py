# Generated by Django 3.1.7 on 2021-04-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='student_answer',
            field=models.CharField(max_length=250),
        ),
    ]
