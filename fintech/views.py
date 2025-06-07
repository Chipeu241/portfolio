from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Danhmuc, Comment
from .forms import CommentForm, CreateUserForm
import json 
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
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
# Xử lý tìm kiếm thông minh
def search(request):
    query = request.GET.get('q', '').strip().lower()

    data = [
        {
            'title': 'Chung kết Startup BA 2024: Sáng tạo và Bùng nổ',
            'content': 'cuộc thi startup sinh viên khởi nghiệp fintech ngân hàng sáng tạo',
            'url': '/cuocthi1/'
        },
        {
            'title': 'Hội chợ việc làm – Cầu nối nhân lực 2025',
            'content': 'việc làm tuyển dụng sinh viên hội chợ ngân hàng doanh nghiệp',
            'url': '/cuocthi2/'
        },
        {
            'title': 'Tọa đàm Fintech: Nắm bắt để thành công bền vững',
            'content': 'fintech hội thảo trực tuyến công nghệ tài chính tương lai',
            'url': '/cuocthi3/'
        },
        {
            'title': 'CHÀO MỪNG NGÀY KHOA HỌC VÀ CÔNG NGHỆ VIỆT NAM 18/5/2025',
            'content': 'ngày khoa học công nghệ việt nam học viện ngân hàng',
            'url': '/tintuc1/'
        },
        {
            'title': 'Khóa luận tốt nghiệp học kỳ II năm học 2024-2025',
            'content': 'nộp khóa luận tốt nghiệp khoa tài chính năm học',
            'url': '/tintuc2/'
        },
        {
            'title': 'PTIT đẩy mạnh đào tạo Fintech trong kỷ nguyên số',
            'content': 'ptit fintech công nghệ đào tạo sinh viên chuyển đổi số',
            'url': '/tintuc3/'
        },
    ]

    for post in data:
        if query in post['title'].lower() or query in post['content'].lower():
            return redirect(post['url'])

    mapping = {
        'giảng viên': 'giangvien',
        'giang vien': 'giangvien',
        'tuyển sinh': 'dh',
        'đại học': 'dh',
        'sau đại học': 'sdh',
        'học phí': 'hocphi',
        'chương trình đào tạo': 'ctdt',
        'đào tạo': 'ctdt',
        'giới thiệu': 'about',
        'tin tức': 'tintuc',
        'cuộc thi': 'cuocthi',
        'sự kiện': 'cuocthi',
        'hội thảo': 'cuocthi',
        'trang chủ': 'index',
    }

    for keyword, view_name in mapping.items():
        if keyword in query:
            return redirect(view_name)

    return render(request, 'fintech/search.html', {'ket_qua': [], 'query': query})

def dky(request):
    return render(request, 'fintech/dky.html')

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        # Bạn có thể lưu dữ liệu ở đây nếu muốn
        # Ví dụ:
        # hoten = request.POST['hoten']
        return redirect('thanhcong')  # Chuyển hướng tới trang thành công
    return redirect('dky')

def thanhcong(request):
    return render(request, 'fintech/thanhcong.html')
def dky(request):
    return render(request, 'fintech/dky.html')
def tintuc(request):
    danhmucs = Danhmuc.objects.filter(loai='tintuc')
    posts = Post.objects.filter(status='published', danhmuc__loai='tintuc')
    return render(request, 'fintech/tintuc.html', {'posts': posts, 'danhmucs': danhmucs})
def cuocthi(request):
    danhmucs = Danhmuc.objects.filter(loai='cuocthi')
    posts = Post.objects.filter(status='published', danhmuc__loai='cuocthi')
    return render(request, 'fintech/cuocthi.html', {'posts': posts, 'danhmucs': danhmucs})
def detail(request, ordering):
    post = get_object_or_404(Post, ordering=ordering)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_cmt = form.save(commit=False)
            new_cmt.post = post
            new_cmt.save()
            return redirect('detail', ordering=post.ordering)
    else:
        form = CommentForm()

    return render(request, 'fintech/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # đăng nhập ngay sau khi đăng ký
            return redirect('profile')  # chuyển sang profile
    else:
        form = CreateUserForm()
    
    context = {'form': form}
    return render(request, 'fintech/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dky')  # nếu đã đăng nhập thì chuyển hướng

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dky')  # chuyển đến dky nếu login thành công
        else:
            messages.info(request, 'user or password not correct!')

    context = {}
    return render(request, 'fintech/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'fintech/profile.html', {'user': request.user})

