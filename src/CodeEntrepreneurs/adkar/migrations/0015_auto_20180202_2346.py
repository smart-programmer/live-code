# Generated by Django 2.0 on 2018-02-02 20:46

import adkar.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0014_auto_20180121_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='body',
            field=models.TextField(blank=True, null=True, validators=[adkar.validators.validate_body]),
        ),
    ]