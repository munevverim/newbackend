# Generated by Django 5.0.1 on 2024-03-29 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quviapi', '0008_alter_userprofile_google_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
