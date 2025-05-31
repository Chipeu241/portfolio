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
]