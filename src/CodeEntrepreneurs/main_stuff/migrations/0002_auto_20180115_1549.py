# Generated by Django 2.0 on 2018-01-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_stuff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='time_of_updateing',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
