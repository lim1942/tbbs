# Generated by Django 3.0 on 2021-07-29 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20210729_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_username',
            field=models.CharField(max_length=63, null=True, verbose_name='父评论用户名'),
        ),
    ]
