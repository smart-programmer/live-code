# Generated by Django 2.0 on 2018-01-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adkar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type_of_content', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('time_of_addition', models.DateTimeField(auto_now=True)),
                ('time_of_updateing', models.DateTimeField(auto_now_add=True)),
                ('my_date', models.DateTimeField()),
            ],
        ),
    ]