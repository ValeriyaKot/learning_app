# Generated by Django 3.1.7 on 2021-04-05 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210405_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='title',
            new_name='module_title',
        ),
        migrations.RemoveField(
            model_name='material',
            name='title',
        ),
    ]