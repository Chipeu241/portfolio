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
    path('tintuc1/', views.tintuc1, name='tintuc1'),
    path('tintuc2/', views.tintuc2, name='tintuc2'),
    path('tintuc3/', views.tintuc3, name='tintuc3'),
    path('cuocthi1/', views.cuocthi1, name='cuocthi1'),
    path('cuocthi2/', views.cuocthi2, name='cuocthi2'),
    path('cuocthi3/', views.cuocthi3, name='cuocthi3'),
    path('search/', views.search, name='search'),
    path('thanhcong/', views.thanhcong, name='thanhcong'),
    path('submit/', views.submit, name='submit'),  # Xử lý form
]