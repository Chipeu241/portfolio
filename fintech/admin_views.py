from django.shortcuts import render
from .models import Post, Comment, Danhmuc
from django.db.models import Count
from datetime import datetime, timedelta

def admin_dashboard(request):
    total_posts = Post.objects.count()
    total_comments = Comment.objects.count()
    top_posts = Post.objects.order_by('-views')[:5]
    post_view_data = Post.objects.values('title', 'views')

    context = {
        'total_posts': total_posts,
        'total_comments': total_comments,
        'top_posts': top_posts,
        'post_view_data': list(post_view_data),
    }
    return render(request, 'fintech/dashboard.html', context)
