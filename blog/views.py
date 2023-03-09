from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic import UpdateView

from accounts.forms import LoginForm, RegisterForm
from .models import Post
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView


class LoginViewForm(FormView):
    form_class = AuthenticationForm
    template_name = "blog/login.html"
    success_message = "Login successful"
    success_url = reverse_lazy("blog:home")
    error_message = "Login False!"

    def form_valid(self, form):
        # We log the user in and redirect to the home page.
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_message = "Registration successful"
    success_url = reverse_lazy("blog:home")
    error_message = "Registration False!"

    def form_valid(self, form):
        user = form.save()
        user = authenticate(self.request, username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


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
    context_object_name = "user_update"
    template_name = "blog/user_update.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    fields = ["email", "mobile", "address", "age", "gender", "biography", "location", "website"]
    success_message = "Profile Updated"

    # def test_func(self):
    #     user = self.get_object()
    #     return self.request.user == user.username

    def get_success_url(self):
        username = self.object.username
        return reverse_lazy("blog:user_profile", kwargs={"username": username})


# @login_required
# def navbar(request):
#     if request.user.is_authenticated:
#         return render(request, 'blog/navbar.html', {'loggedin': True})
#     else:
#         return render(request, 'blog/navbar.html', {'loggedin': False})
