from django import forms
from blog.views import Post
from martor.fields import MartorFormField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
