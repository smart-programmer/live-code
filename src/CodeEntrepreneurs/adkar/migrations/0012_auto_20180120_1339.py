# Generated by Django 2.0 on 2018-01-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0011_auto_20180120_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
