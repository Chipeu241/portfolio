from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Danhmuc, Comment, taiKhoan
from .forms import CommentForm, CreateUserForm, DangKyTuyenSinhForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.timezone import now, timedelta
from django.db.models.functions import TruncDay
from django.db.models import Count

def index(request):
    return render(request, 'fintech/index.html')

def about(request):
    return render(request, 'fintech/about.html')

def giangvien(request):
    return render(request, 'fintech/GV.html')

def ctdt(request):
    return render(request, 'fintech/ctdt.html')

def hocphi(request):
    return render(request, 'fintech/hocphi.html')

def dh(request):
    return render(request, 'fintech/dh.html')

def sdh(request):
    return render(request, 'fintech/sdh.html')

def noibo(request):
    danhmucs = Danhmuc.objects.filter(loai='noibo')
    posts = Post.objects.filter(status='published', danhmuc__loai='noibo')
    return render(request, 'fintech/noibo.html', {'posts': posts, 'danhmucs': danhmucs})

def quocte(request):
    danhmucs = Danhmuc.objects.filter(loai='quocte')
    posts = Post.objects.filter(status='published', danhmuc__loai='quocte')
    return render(request, 'fintech/quocte.html', {'posts': posts, 'danhmucs': danhmucs})

def detail(request, ordering):
    post = get_object_or_404(Post, ordering=ordering)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login') 
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('detail', ordering=post.ordering)
    else:
        form = CommentForm()
    return render(request, 'fintech/detail.html', {'post': post, 'comments': comments, 'form': form})

def search(request):
    query = request.GET.get('q', '').strip()
    ket_qua = []

    if query:
        ket_qua = Post.objects.filter(
            Q(status='published') &
            (Q(title__icontains=query) | Q(content__icontains=query))
        ).distinct()

    return render(request, 'fintech/search.html', {'ket_qua': ket_qua, 'query': query})

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        form = DangKyTuyenSinhForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanhcong')
        else:
            return render(request, 'fintech/dky.html', {'form': form})
    return redirect('dky')

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Đăng ký thất bại. Vui lòng kiểm tra lại thông tin.')
    else:
        form = CreateUserForm()
    return render(request, 'fintech/register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'user or password not correct!')
    return render(request, 'fintech/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'fintech/profile.html', {'user': request.user})

@staff_member_required
def baocao_view(request):
    total_posts = Post.objects.count()
    total_comments = Comment.objects.count()
    total_users = taiKhoan.objects.count()
    total_views = Post.objects.aggregate(total=Count('views'))['total'] or 0
    today = now().date()
    posts_by_day = (
        Post.objects.filter(publish_date__gte=today - timedelta(days=7))
        .annotate(day=TruncDay('publish_date'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    return render(request, 'baocao.html', {
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_users': total_users,
        'total_views': total_views,
        'posts_by_day': posts_by_day,
    })
