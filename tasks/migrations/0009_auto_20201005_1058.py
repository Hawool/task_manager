# Generated by Django 3.1.2 on 2020-10-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20201005_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='stat',
            field=models.CharField(choices=[('New', 'New'), ('Planned', 'Planned'), ('In hand', 'In hand'), ('Completed', 'Completed')], default='NW', max_length=10),
        ),
    ]
