# Generated by Django 5.0.7 on 2024-08-24 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_otp_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_verify',
            new_name='is_verified',
        ),
    ]
