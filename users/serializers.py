import re
from rest_framework import serializers


from users import models


class UserSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if not re.match(r"^[\da-zA-Z]{5,20}$",value):
            raise serializers.ValidationError('username 只能使用字母和数字，长度在5~20之间')

    def validate_password(self, value):
        if not re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$",value):
            raise serializers.ValidationError('password 长度在8~20之间，至少包含一个大写、一个小写、一个数字、一个特殊符号')

    def validate_email(self, value):
        """使用email 字段自带校验"""
        pass

    def create(self, validated_data):
        return super().create(validated_data)


    class Meta:
        model = models.User
        fields = '__all__'