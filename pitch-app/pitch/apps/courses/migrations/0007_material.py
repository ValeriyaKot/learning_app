# Generated by Django 3.1.7 on 2021-04-05 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_delete_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('text', models.TextField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.module')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
