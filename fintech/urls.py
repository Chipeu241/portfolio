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
    path('tintuc1/', views.tintuc1_view, name='tintuc1'),
    path('tintuc2/', views.tintuc2_view, name='tintuc2'),
    path('tintuc3/', views.tintuc3_view, name='tintuc3'),
    path('cuocthi1/', views.cuocthi1_view, name='cuocthi1'),
    path('cuocthi2/', views.cuocthi2_view, name='cuocthi2'),
    path('cuocthi3/', views.cuocthi3_view, name='cuocthi3'),
]