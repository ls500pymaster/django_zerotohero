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
    class Meta:
        model = Comments
        fields = ["body"]

# class ScheduleEmailForm(forms.Form):
#     # name = forms.CharField(label='Name', max_length=100)
#     # email = forms.EmailField(label='Email', max_length=100)
#     # subject = forms.CharField(label='Subject', max_length=100)
#     # message = forms.CharField(label='Message', widget=forms.Textarea)
#     # date = forms.DateTimeField(label='Date and Time', input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#
#     def send_email(self, date):
#         # name = [self.cleaned_data['name']]
#         # email = self.cleaned_data['email']
#         # subject = self.cleaned_data['subject']
#         # message = self.cleaned_data['message']
#         # date_at = self.cleaned_data['date']
#         send_feedback_email_task.apply_async(**date)