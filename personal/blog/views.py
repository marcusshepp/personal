from django.shortcuts import render, redirect

from rest_framework import viewsets

from .models import (
    Post,
    Comment,
    Category,
)
from .serializers import (
    PostSerializer,
    CommentSerializer,
    CategorySerializer,
)


def blog_landing(request):
    return render(request, "blog/landing.html")
    
    
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer