from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
