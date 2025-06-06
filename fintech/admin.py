from django.contrib import admin
from .models import taiKhoan, Post, Danhmuc
# Register your models here.

admin.register(taiKhoan)
class TaiKhoanAdmin(admin.ModelAdmin):
    list_display = ['tenTaiKhoan', 'hoTen', 'email', 'soDienThoai', 'create_at']
    search_fields = ['tenTaiKhoan', 'email', 'soDienThoai']
admin.site.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'status', 'ordering')
    list_filter = ["status"]
    search_fields = ["title"]

class DanhmucAdmin(admin.ModelAdmin):
    list_display = ('ten', 'loai')
    list_filter = ('loai',)
admin.site.register(Danhmuc, DanhmucAdmin)