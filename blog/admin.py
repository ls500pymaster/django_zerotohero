from django.contrib import admin
from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from blog.models import Post, UserProfile, Comments, Tag, Category
from martor.widgets import AdminMartorWidget
# from accounts.models import CustomUser

admin.site.site_url = "/blog"


@admin.register(Category)
class PostCategory(admin.ModelAdmin):
    list_display = ("name",)


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
    list_display = ("user", "post", "created", "approved", )
    list_filter = ("user", "approved",)
    search_fields = ("user", "body",)
    actions = ["approve_comments"]

    def approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
