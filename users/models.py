from django.db import models


class User(models.Model):
    username = models.CharField("用户名",max_length=63,null=False,unique=True)
    password = models.CharField("密码",max_length=63,null=False)
    email = models.EmailField("邮箱",null=False,unique=True)
    updated_time = models.DateTimeField("更新时间",auto_now=True)
    created_time = models.DateTimeField("创建时间",auto_now_add=True)

    def __str__(self):
        return self.username
