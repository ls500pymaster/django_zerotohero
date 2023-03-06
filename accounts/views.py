from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy


from accounts.forms import LoginForm, RegisterForm
from blog.models import UserProfile


class LoginView(auth_views.LoginView):
	form_class = LoginForm
	template_name = "accounts/login.html"
	success_url = reverse_lazy("blog:post_list")


class RegisterView(generic.CreateView):
	form_class = RegisterForm
	template_name = "accounts/register.html"
	success_url = reverse_lazy("blog:post_list")


