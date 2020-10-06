# Generated by Django 3.1.2 on 2020-10-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20201005_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_planned',
            field=models.DateTimeField(null=True, verbose_name='Planned finish time (YYYY-MM-DD HH-MM-SS):'),
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
