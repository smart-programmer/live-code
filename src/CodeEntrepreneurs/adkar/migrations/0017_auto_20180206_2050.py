# Generated by Django 2.0 on 2018-02-06 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adkar', '0016_adkar_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkar',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]