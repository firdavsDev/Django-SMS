# Generated by Django 4.0.6 on 2022-07-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=35)),
                ('code', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='SmsToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('created_at', models.DateField()),
                ('expires_at', models.DateField()),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Token',
                'ordering': ('-id',),
            },
        ),
    ]
