from django.db import models
from users.models import User


class Comment(models.Model):
    msg = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING)
    root = models.ForeignKey('self', related_name='root_comment', null=True, blank=True, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', related_name='parent_comment', blank=True, null=True,
                               on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        if len(self.msg) <= 10:
            return self.msg
        else:
            return self.msg[:10] + '...'
