from django.shortcuts import render
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