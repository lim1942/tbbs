import re
from rest_framework import serializers

from users import models
from users import tools


class UserSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if not re.match(r"^[\da-zA-Z]{5,20}$", value):
            raise serializers.ValidationError('username 只能使用字母和数字，长度在5~20之间')
        return value

    def validate_password(self, value):
        if not re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$", value):
            raise serializers.ValidationError('password 长度在8~20之间，至少包含一个大写、一个小写、一个数字、一个特殊符号')
        return value

    def validate_email(self, value):
        """使用email 字段自带校验"""
        return value

    def create(self, validated_data):
        validated_data['password'] = tools.get_md5(validated_data['password'])
        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(**validated_data)
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password')
        return ret

    class Meta:
        model = models.User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username_email = serializers.CharField(label='用户名 或 邮箱', allow_blank=False, allow_null=False)
    password = serializers.CharField(label='密码', allow_blank=False, allow_null=False)
    remember = serializers.BooleanField(label='记住我', initial=False)
