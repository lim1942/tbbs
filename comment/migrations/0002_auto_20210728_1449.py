# Generated by Django 3.2 on 2021-07-28 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_time',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='aa', max_length=63, verbose_name='发布用户'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='msg',
            field=models.CharField(max_length=255, verbose_name='留言消息'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_comment', to='comment.comment', verbose_name='父节点'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_comment', to='comment.comment', verbose_name='根节点'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='users.user', verbose_name='发布用户'),
        ),
    ]