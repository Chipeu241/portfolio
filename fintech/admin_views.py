# fintech/admin_views.py
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def baocao_view(request):
    # Dữ liệu báo cáo giả lập
    context = {
        'views_count': 1024,
        'post_views': 830,
        'comments_count': 154,
        'registrations': 42,
    }
    return render(request, 'admin/baocao.html', context)