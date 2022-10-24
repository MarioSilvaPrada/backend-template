# Generated by Django 4.1.1 on 2022-10-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enodetokenmodel',
            name='expires_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='enodetokenmodel',
            name='expires_in',
            field=models.PositiveIntegerField(max_length=50),
        ),
    ]