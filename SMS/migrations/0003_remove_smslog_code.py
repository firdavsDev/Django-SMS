# Generated by Django 4.0.6 on 2022-07-12 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0002_delete_smstoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smslog',
            name='code',
        ),
    ]
