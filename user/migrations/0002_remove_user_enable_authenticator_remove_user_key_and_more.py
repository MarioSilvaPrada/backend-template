# Generated by Django 4.1.1 on 2022-10-24 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='enable_authenticator',
        ),
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]