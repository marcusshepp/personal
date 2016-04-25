from rest_framework import serializers

from .models import (
    Post,
    Comment,
    Category,
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "placeholder_image",
            "category",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "email",
            "body",
            "post",
            "comments",
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )