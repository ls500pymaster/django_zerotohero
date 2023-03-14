from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.ChoiceField(label='Subject', choices=[
        ('feedback', 'Feedback'),
        ('bug_report', 'Report a bug'),
        ('feature_request', 'Feature request'),
        ('other', 'Other'),
    ])
    message = forms.CharField(label='Message', widget=forms.Textarea)