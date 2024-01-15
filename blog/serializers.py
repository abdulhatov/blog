from rest_framework import serializers
from .models import (
    Blog,
    Like,
    Comment
)


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CreateLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
