# Generated by Django 3.2 on 2021-07-29 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20210728_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_username',
            field=models.CharField(default='aa', max_length=63, verbose_name='父评论用户名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_username',
            field=models.CharField(default='bb', max_length=63, verbose_name='发布用户名'),
            preserve_default=False,
        ),
    ]
