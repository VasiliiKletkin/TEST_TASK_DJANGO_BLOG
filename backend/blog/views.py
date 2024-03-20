from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .forms import CommentForm
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "body", "slug", "author"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["comment_form"] = CommentForm()
        return context_data


class CommentCreateView(CreateView):
    model = Comment
    template_name = "blog/comment_create.html"
    fields = ["post", "body"]

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        kwargs["author"] = request.user
        return super().post(request, *args, **kwargs)