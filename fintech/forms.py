from django import forms
from .models import Comment
from .models import taiKhoan
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'name', 'email']
