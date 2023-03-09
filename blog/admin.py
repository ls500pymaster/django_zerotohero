from django.contrib import admin
from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from blog.models import Post, UserProfile, Comments, Tag
from martor.widgets import AdminMartorWidget
# from accounts.models import CustomUser


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "gender", "age", "development")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    formfield_overrides = {
        MartorField: {'widget': AdminMartorWidget},
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "body", "created", "published")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )

