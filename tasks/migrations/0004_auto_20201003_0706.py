# Generated by Django 3.1.2 on 2020-10-03 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]