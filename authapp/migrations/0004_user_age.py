# Generated by Django 2.2 on 2021-06-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210624_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='Возраст'),
        ),
    ]
