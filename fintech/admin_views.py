from django.shortcuts import render
from .models import Post, Comment, Danhmuc
from django.db.models import Count
from datetime import datetime, timedelta

def admin_dashboard(request):
    total_posts = Post.objects.count()
    total_comments = Comment.objects.count()
    top_posts = Post.objects.order_by('-views')[:5]
    post_view_data = Post.objects.values('title', 'views')

    # ✅ Tách dữ liệu trước khi render template
    titles = [item['title'] for item in post_view_data]
    views = [item['views'] for item in post_view_data]

    context = {
        'total_posts': total_posts,
        'total_comments': total_comments,
        'top_posts': top_posts,
        'titles': titles,   # ✅ list tiêu đề
        'views': views      # ✅ list view
    }

    return render(request, 'fintech/dashboard.html', context)