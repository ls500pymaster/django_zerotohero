from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    template_name = "blog/post_list.html"


class PostListDetail(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    paginate_by = 5
    template_name = "blog/post_detail.html"


class PostCreate(generic.CreateView):
    model = Post
    context_object_name = "post_create"
    template_name = "blog/post_create.html"
    fields = ["title", "body", "tags", "image",]


