# Generated by Django 2.0 on 2018-01-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0002_remove_adkar_my_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]