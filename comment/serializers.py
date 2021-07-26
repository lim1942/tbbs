from rest_framework import serializers

from comment import models


class CommentSerializer(serializers.ModelSerializer):

    def validate_msg(self, value):
        if len(value) < 3 or len(value) > 20:
            raise serializers.ValidationError('字数必须在3~200字之间')
        return value

    class Meta:
        model = models.Comment
        fields = '__all__'
