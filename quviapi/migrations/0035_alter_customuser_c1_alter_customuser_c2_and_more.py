# Generated by Django 4.2.11 on 2024-04-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quviapi', '0034_alter_customuser_c1_alter_customuser_c2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='c1',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='c2',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='c3',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='c4',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='c5',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
