# Generated by Django 2.0 on 2018-01-19 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0006_remove_adkar_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adkar',
            old_name='time_of_updateing',
            new_name='time_of_updating',
        ),
    ]
