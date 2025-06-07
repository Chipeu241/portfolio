from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
# Create your models here.
class taiKhoan(User):
    class Meta:
        proxy = True
        verbose_name = 'Tài khoản người dùng'
        verbose_name_plural = 'Tài khoản người dùng'

 
class Danhmuc(models.Model):
    LAYOUT_CHOICE=(
        ('list','List'),
        ('grid','Grid')
    )
    ten=models.CharField(unique=True, max_length=100)
    ordering=models.IntegerField(default=0)
    loai = models.CharField(max_length=20,choices=(('tintuc', 'Tin tức'), ('cuocthi', 'Cuộc thi')), default='tintuc')
    layout=models.CharField(max_length=10,choices=LAYOUT_CHOICE)
    def __str__(self):
        return self.ten

from ckeditor.fields import RichTextField
class Post(models.Model):
    STATUS_CHOICE=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=100)
    danhmuc=models.ForeignKey(Danhmuc, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE, default='draft')
    ordering=models.IntegerField(default=0)
    content=RichTextField(default='Nội dung đang cập nhật')
    publish_date=models.DateTimeField()
    image=models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
#change register form
    class CreateUserForm(UserCreationForm):
      class Meta:
        model = User  
        fields = ['username', 'email', 'first_name','last_name','password1','password2' ]       