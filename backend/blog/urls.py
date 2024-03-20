from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path(
        "posts/<int:pk>/comments/new",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),
]
