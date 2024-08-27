# Generated by Django 5.0.3 on 2024-04-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quviapi', '0013_remove_userprofile_profile_picture_userprofile_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='token',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='html_file',
            field=models.FileField(blank=True, null=True, upload_to='html_files/'),
        ),
    ]
