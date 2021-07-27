from rest_framework import serializers

from comment import models


class CommentSerializer(serializers.ModelSerializer):

    def validate_msg(self, value):
        if len(value) < 3 or len(value) > 20:
            raise serializers.ValidationError('字数必须在3~200字之间')
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user_item
        parent = validated_data['parent']
        if parent:
            validated_data['root'] = parent.root or parent
        else:
            validated_data['root'] = None
        return super().create(validated_data)

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['user', 'root']

