# Generated by Django 2.1.7 on 2019-03-15 13:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='liked',
            field=models.ManyToManyField(related_name='liked_news', to=settings.AUTH_USER_MODEL, verbose_name='点赞用户'),
        ),
    ]
