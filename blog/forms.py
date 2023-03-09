from django import forms

from blog.models import UserProfile
from blog.models import Comments
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from mdeditor.fields import MDTextField

from blog.views import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', "status",]


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ["mobile", "address", "age", "gender", "biography", "location", "website", "avatar"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email / Username")


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ["mobile", "address", "age", "gender", "biography", "location", "website", "avatar", "development"]


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=False)
    body = MDTextField()

    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')

