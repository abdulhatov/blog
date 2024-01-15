from rest_framework import generics
from .models import (
    Blog,
    Like,
    Comment,
)

from .serializers import (
    CreateBlogSerializer,
    CreateLikeSerializer,
)


class CreateBlogView(generics.CreateAPIView):
    serializer_class = CreateBlogSerializer
    queryset = Blog.objects.all()


class CreateLikeView(generics.CreateAPIView):
    serializer_class = CreateLikeSerializer
    queryset = Like.objects.all()
