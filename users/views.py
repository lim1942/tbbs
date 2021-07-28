import uuid
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from django.contrib.sessions.models import Session
from rest_framework import viewsets, mixins, views, response

from users import tools
from users import models, serializers


class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class LoginView(views.APIView):

    def get_serializer(self, *args, **kwargs):
        return serializers.LoginSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username_email = serializer.data['username_email']
        password = serializer.data['password']
        remember = serializer.data['remember']
        user_find = models.User.objects.filter(Q(username=username_email) | Q(email=username_email)).all()
        if user_find:
            user = user_find[0]
            if tools.get_md5(password) == user.password:
                resp = response.Response({'status': 0, 'msg': '登录成功','info':user.info},status=201)
                session_key = uuid.uuid4().hex
                if remember:
                    # cookie 在浏览器的有效期 和 session 在服务器的 期限都为 30天
                    max_age = 30 * 24 * 3600
                    resp.set_cookie('session_key', session_key, max_age=max_age)
                else:
                    # 关闭浏览器cookie失效，session 有效期为1天
                    max_age = 3600 * 24
                    resp.set_cookie('session_key', session_key)
                session_expire_date = timezone.now() + timedelta(seconds=max_age)
                Session.objects.create(session_key=session_key, session_data=user.info, expire_date=session_expire_date)
                return resp
            else:
                return response.Response({'status': 101, 'msg': '密码错误'},status=400)
        else:
            return response.Response({'status': 102, 'msg': '用户不存在'},status=400)

    def get(self, request, *args, **kwargs):
        return response.Response({'msg': '登录接口'})
