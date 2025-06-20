# Generated by Django 4.1.7 on 2025-06-08 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fintech', '0006_alter_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DangKyTuyenSinh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_ten', models.CharField(max_length=100, verbose_name='Họ và tên')),
                ('ngay_sinh', models.DateField(verbose_name='Ngày sinh')),
                ('gioi_tinh', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=10, verbose_name='Giới tính')),
                ('so_dien_thoai', models.CharField(max_length=15, verbose_name='Số điện thoại')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('dia_chi', models.TextField(verbose_name='Địa chỉ')),
                ('ngay_dang_ky', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian đăng ký')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người đăng ký')),
            ],
        ),
    ]
