from rest_framework import serializers

from comment import models


class CommentSerializer(serializers.ModelSerializer):

    def validate_msg(self, value):
        if len(value) < 3 or len(value) > 20:
            raise serializers.ValidationError('字数必须在3~200字之间')
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user_item
        validated_data['pub_username'] = validated_data['user'].username
        parent = validated_data['parent']
        if parent:
            validated_data['parent_username'] = parent.user.username
            validated_data['root'] = parent.root or parent
        else:
            validated_data['parent_username'] = None
            validated_data['root'] = None
        return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context['request']
        ret = super().to_representation(instance)
        if ret['root'] is None:
            ret['child_cnt'] = models.Comment.objects.filter(root=ret['id']).count()
            ret['child_url'] = request._request.build_absolute_uri(f'?root={ret["id"]}')
        return ret

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['user','root','pub_username','parent_username']

