# Generated by Django 2.0 on 2018-05-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0019_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activation',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
