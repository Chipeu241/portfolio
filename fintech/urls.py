from django.urls import path
from . import views, admin_views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('giangvien/', views.giangvien, name='giangvien'),
    path('ctdt/', views.ctdt, name='ctdt'),
    path('hocphi/', views.hocphi, name='hocphi'),
    path('dh/', views.dh, name='dh'),
    path('sdh/', views.sdh, name='sdh'),
    path('noibo/', views.noibo, name='noibo'),
    path('quocte/', views.quocte, name='quocte'),
    path('noibo/<int:ordering>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('dky/', views.dky, name='dky'),  # Trang đăng ký
    path('thanhcong/', views.thanhcong, name='thanhcong'),
    path('submit/', views.submit, name='submit'),  # Xử lý form
    path('register/', views.register, name='register'), 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'), # Xử lý form
    path('profile/', views.profile, name='profile'),
    path('admin/baocao/', admin_views.baocao_view, name='admin_baocao'),
]