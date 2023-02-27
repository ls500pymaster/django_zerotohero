from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    template_name = "post_list.html"


class PostListDetail(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    paginate_by = 5
    template_name = "templates/post_detail.html"