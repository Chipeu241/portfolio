from django.contrib import admin
from .models import taiKhoan, Post, Danhmuc
# Register your models here.
admin.site.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'status', 'ordering')
    list_filter = ["status"]
    search_fields = ["title"]

class DanhmucAdmin(admin.ModelAdmin):
    list_display = ('ten', 'loai')
    list_filter = ('loai',)
admin.site.register(Danhmuc, DanhmucAdmin)

class TaiKhoanAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=False)  # chỉ user thường
admin.site.register(taiKhoan, TaiKhoanAdmin)