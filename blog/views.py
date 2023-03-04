from django.shortcuts import render, get_object_or_404
from .models import Post, UserProfile
from django.views import generic
from django.contrib.auth.decorators import login_required


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    paginate_by = 5
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "blog/post_detail.html"


class PostCreate(generic.CreateView):
    model = Post
    context_object_name = "post_create"
    template_name = "blog/post_create.html"
    fields = ["title", "body", "tags", "image",]


class UserListView(generic.ListView):
    model = UserProfile
    context_object_name = "user_list"
    template_name = "blog/user_list.html"


@login_required()
class UserDetailView(generic.DetailView):
    model = UserProfile
    context_object_name = "user_detail"
    template_name = "blog/user_detail.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        return get_object_or_404(UserProfile, user__username=username)


