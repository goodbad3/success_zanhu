# Generated by Django 2.1.7 on 2019-05-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('messager', '0002_auto_20190523_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='unread',
            field=models.BooleanField(default=True, verbose_name='是否未读'),
        ),
    ]
