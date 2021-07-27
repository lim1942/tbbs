from django.db import models
from users.models import User


class Comment(models.Model):
    msg = models.CharField(max_length=255, verbose_name='留言消息')
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING, verbose_name='发布用户')
    root = models.ForeignKey('self', related_name='root_comment', null=True, blank=True,
                             on_delete=models.DO_NOTHING,verbose_name='根节点')
    parent = models.ForeignKey('self', related_name='parent_comment', blank=True, null=True,
                               on_delete=models.DO_NOTHING, verbose_name='父节点')
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        if len(self.msg) <= 10:
            return self.msg
        else:
            return self.msg[:10] + '...'

    class Meta:
        ordering = ('-created_time',)