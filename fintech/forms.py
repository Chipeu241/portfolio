from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User  
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']