from django import forms
from django.contrib.auth.views import LoginView
from blog.models import UserProfile, Category, Post
from blog.models import Comments
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from mdeditor.fields import MDTextField


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'tags', 'image', 'status']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["mobile", "address", "age", "gender", "biography", "location", "website", "avatar"]


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ["mobile", "address", "age", "gender", "biography", "location", "website", "avatar", "development"]


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = Comments
        fields = ["body",]
