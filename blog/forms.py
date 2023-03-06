from django import forms
from blog.views import Post
from martor.fields import MartorFormField
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']


# class EmailAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(
#         widget=forms.TextInput(attrs={'autofocus': True}),
#         label="Email",
#     )
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput,
#     )
#
#     error_messages = {
#         'invalid_login': (
#             "Please enter a correct email and password. "
#             "Note that both fields may be case-sensitive."
#         ),
#         'inactive': "This account is inactive.",
#     }
#
#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user is None:
#                 raise forms.ValidationError(
#                     self.error_messages['invalid_login'],
#                     code='invalid_login',
#                     params={'email': self.username_field.verbose_name},
#                 )
#             elif not user.is_active:
#                 raise forms.ValidationError(
#                     self.error_messages['inactive'],
#                     code='inactive',
#                 )
#         return self.cleaned_data