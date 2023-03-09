from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic import UpdateView

from accounts.forms import LoginForm, RegisterForm
from .models import Post
from .models import UserProfile


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "blog/login.html"
    success_message = "Login successful"
    success_url = reverse_lazy("blog:user_profile")
    error_message = "Login False!"


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_message = "Registration successful"
    success_url = reverse_lazy("blog:user_list")
    error_message = "Registration False!"


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    template_name = "blog/post_list.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    paginate_by = 5
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "blog/post_detail.html"


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    context_object_name = "post_create"
    template_name = "blog/post_create.html"
    fields = ["title", "body", "tags", "image", "status"]
    success_url = reverse_lazy("blog:post_detail")


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = "post_update"
    template_name = "blog/post_update.html"
    fields = ["title", "body", "tags", "image"]
    success_message = "Post updated"

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})


class UserListView(generic.ListView):
    model = UserProfile
    context_object_name = "user_list"
    paginate_by = 5
    template_name = "blog/user_list.html"


class UserDetailView(DetailView):
    model = UserProfile
    context_object_name = "user_detail"
    template_name = "blog/user_detail.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        return get_object_or_404(UserProfile, username=username)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'blog/user_profile.html'


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "user_posts"
    template_name = "blog/user_posts.html"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).order_by("-created")


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user_update"
    template_name = "blog/user_update.html"
    fields = ["email", "mobile", "address", "age", "gender", "biography", "location", "website"]
    success_message = "Profile Updated"

    def get_success_url(self):
        username = self.object.username
        return reverse_lazy("blog:user_profile", kwargs={"username": username})


@login_required
def navbar(request):
    if request.user.is_authenticated:
        return render(request, 'blog/navbar.html', {'loggedin': True})
    else:
        return render(request, 'blog/navbar.html', {'loggedin': False})
