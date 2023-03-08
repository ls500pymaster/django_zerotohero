from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import LoginForm, RegisterForm
from blog.models import UserProfile

