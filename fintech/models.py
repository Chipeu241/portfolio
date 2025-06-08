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
    loai = models.CharField(max_length=20,choices=(('noibo', 'Tin tức nội bộ'), ('quocte', 'Tin tức quốc tế')), default='noibo')
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
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  # 🔗 Liên kết với tài khoản
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
#change register form
class CreateUserForm(UserCreationForm):
      class Meta:
        model = User  
        fields = ['username', 'email', 'first_name','last_name','password1','password2']

class DangKyTuyenSinh(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Người đăng ký")
    ho_ten = models.CharField("Họ và tên", max_length=100)
    ngay_sinh = models.DateField("Ngày sinh")
    gioi_tinh = models.CharField("Giới tính", max_length=10, choices=(('Nam', 'Nam'), ('Nữ', 'Nữ')))
    so_dien_thoai = models.CharField("Số điện thoại", max_length=15)
    email = models.EmailField("Email")
    dia_chi = models.TextField("Địa chỉ")
    ngay_dang_ky = models.DateTimeField("Thời gian đăng ký", auto_now_add=True)

    def __str__(self):
        return f"{self.ho_ten} - Công nghệ tài chính"