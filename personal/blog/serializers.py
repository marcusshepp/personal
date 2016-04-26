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
            "get_category_name",
            "id",
            "display_date_created",
            "get_body_preview",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "email",
            "body",
            "post",
            "comments",
            "id",
            "display_date_created",
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "id",
            "display_date_created",
        )
