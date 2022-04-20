from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField()
    created = serializers.DateTimeField(
        required=False, format="%Y-%m-%d %H:%M:%S", )

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
