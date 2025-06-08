from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DangKyTuyenSinh
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
class DangKyTuyenSinhForm(forms.ModelForm):
    class Meta:
        model = DangKyTuyenSinh
        fields = ['ho_ten', 'ngay_sinh', 'gioi_tinh', 'so_dien_thoai', 'email', 'dia_chi']
        widgets = {
            'ngay_sinh': forms.DateInput(attrs={'type': 'date'}),
        }