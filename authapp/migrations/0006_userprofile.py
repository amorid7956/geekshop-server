# Generated by Django 3.1.1 on 2021-06-24 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210624_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='Тэги')),
                ('about_me', models.TextField(blank=True, max_length=512, verbose_name='О себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('W', 'W')], max_length=1, verbose_name='Пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]