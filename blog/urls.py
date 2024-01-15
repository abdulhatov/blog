from django.urls import path
from .views import (
    CreateBlogView,
    CreateLikeView,
)

urlpatterns = [
    path('create/', CreateBlogView.as_view()),
    path('like/create/', CreateLikeView.as_view())
]
