# Generated by Django 2.0 on 2018-01-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0012_auto_20180120_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adkar',
            name='type_of_content',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
