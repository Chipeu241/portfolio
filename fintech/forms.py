from django import forms
from .models import Comment
from .models import taiKhoan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'name', 'email']
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = taiKhoan
        fields = ['tenTaiKhoan', 'matKhau', 'hoTen', 'email', 'soDienThoai', 'diaChi']
        widgets = {
            'matKhau': forms.PasswordInput(),
        }