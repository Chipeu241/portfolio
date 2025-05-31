from django.db import models

# Create your models here.
class taiKhoan(models.Model):
    tenTaiKhoan = models.CharField(max_length=50)
    matKhau = models.CharField(max_length=50)
    hoTen = models.CharField(max_length=50)
    email = models.EmailField()
    soDienThoai = models.CharField(max_length=15)
    diaChi = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #trangThai = models.BooleanField(default=True)

    def __str__(self):
        return self.tenTaiKhoan