from django.urls import path
from . import views
from . import admin_views
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
    path('quocte/<int:ordering>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('submit/', views.submit, name='submit'),  # Xử lý form
    path('register/', views.register, name='register'), 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'), # Xử lý form
    path('profile/', views.profile, name='profile'),
    path('dashboard/', admin_views.admin_dashboard, name='admin-dashboard'),
]
