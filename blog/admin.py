from django.contrib import admin
from blog.models import Post, UserProfile, Comments, Tag


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "gender", "age")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "status")


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "body", "created", "published")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
