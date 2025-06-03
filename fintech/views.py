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