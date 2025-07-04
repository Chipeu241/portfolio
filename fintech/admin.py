from django.contrib import admin
from .models import taiKhoan, Post, Danhmuc
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
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

class DummyReportModel:
    class _meta:
        app_label = 'fintech'
        model_name = 'baocaothongke'
        verbose_name = 'Báo cáo thống kê'
        verbose_name_plural = 'Báo cáo thống kê'

    def __str__(self):
        return "Báo cáo thống kê"

class ReportAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return redirect(reverse('admin_baocao'))

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return True

from .models import Comment
class ReplyInline(admin.TabularInline):
    model = Comment
    fk_name = 'parent'
    extra = 1
    verbose_name = "Phản hồi"
    verbose_name_plural = "Các phản hồi"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')
    inlines=[ReplyInline]

admin.site.register(Comment, CommentAdmin)
