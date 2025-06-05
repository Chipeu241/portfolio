from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('giangvien/', views.giangvien, name='giangvien'),
    path('ctdt/', views.ctdt, name='ctdt'),
    path('hocphi/', views.hocphi, name='hocphi'),
    path('dh/', views.dh, name='dh'),
    path('sdh/', views.sdh, name='sdh'),
    path('tintuc/', views.tintuc, name='tintuc'),
    path('cuocthi/', views.cuocthi, name='cuocthi'),
    path('tintuc/<int:ordering>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('dky/', views.dky, name='dky'),  # Trang đăng ký
    path('thanhcong/', views.thanhcong, name='thanhcong'),
    path('submit/', views.submit, name='submit'),  # Xử lý form
]