import time
import json

from django.db import models


class User(models.Model):
    username = models.CharField("用户名", max_length=63, null=False, unique=True)
    email = models.EmailField("邮箱", null=False, unique=True)
    password = models.CharField("密码", max_length=63, null=False)
    updated_time = models.DateTimeField("更新时间", auto_now=True)
    created_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.username

    @property
    def info(self):
        return json.dumps(
            {'username': self.username,
             'email': self.email,
             'created_time': int(self.created_time.timestamp()),
             't': int(time.time())
             }
        )

    class Meta:
        ordering = ('-created_time',)
