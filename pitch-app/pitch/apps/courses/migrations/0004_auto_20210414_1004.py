# Generated by Django 3.1.7 on 2021-04-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_testresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='test',
        ),
        migrations.RemoveField(
            model_name='test',
            name='course',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='test',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]