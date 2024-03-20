from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from model_utils.models import TimeStampedModel

User = get_user_model()


class Post(TimeStampedModel):
    DRAFT = "draft"
    PUBLISHED = "published"

    STATUS_CHOICES = (
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="created")
    body = models.TextField()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    active = models.BooleanField(default=True)
    body = models.TextField()

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment, {self.post}"
