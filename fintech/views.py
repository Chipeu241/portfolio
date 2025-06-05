from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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
def tintuc(request):
    return render(request, 'fintech/tintuc.html')
def cuocthi(request):
    return render(request, 'fintech/cuocthi.html')
def tintuc1(request):
    return render(request, 'fintech/tintuc1.html')
def tintuc2(request):
    return render(request, 'fintech/tintuc2.html')
def tintuc3(request):
    return render(request, 'fintech/tintuc3.html')
def cuocthi1(request):
    return render(request, 'fintech/cuocthi1.html')
def cuocthi2(request):
    return render(request, 'fintech/cuocthi2.html')
def cuocthi3(request):
    return render(request, 'fintech/cuocthi3.html')
# Xử lý tìm kiếm thông minh
def search(request):
    query = request.GET.get('q', '').strip().lower()

    # Trường hợp chuyển thẳng đến bài viết chi tiết
    if any(k in query for k in ['startup', 'startup ba', 'cuộc thi khởi nghiệp', 'ba 2024']):
        return redirect('cuocthi1')
    elif any(k in query for k in ['việc làm', 'hội chợ việc làm', 'cầu nối nhân lực','hội chợ']):
        return redirect('cuocthi2')
    elif any(k in query for k in ['fintech', 'tài chính', 'hội thảo fintech']):
        return redirect('cuocthi3')

    if any(k in query for k in ['ngày khoa học', '18/5', 'công nghệ việt nam']):
        return redirect('tintuc1')
    elif any(k in query for k in ['khóa luận', 'tốt nghiệp', 'nộp khóa luận']):
        return redirect('tintuc2')
    elif any(k in query for k in ['ptit', 'đào tạo fintech', 'điểm chuẩn fintech']):
        return redirect('tintuc3')
    

    # Các từ khóa chuyển hướng trang chung
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
