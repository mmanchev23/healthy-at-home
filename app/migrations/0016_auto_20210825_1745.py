# Generated by Django 3.2.6 on 2021-08-25 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210825_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='github',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='website_link',
        ),
    ]
