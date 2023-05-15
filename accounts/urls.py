"""greatchoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'accounts'

urlpatterns = [
    path('social/signup/', views.signup, name='signup'),
    path('basic_signup/', views.basic_signup, name='basic_signup'),
    path('signup/', views.signup, name='signup'),
    path('kakao/disconnect/', views.kakao_disconnect, name='kakao_disconnect'),
    path('delete/', views.delete, name='delete'),
    path('basic_login/', views.basic_login, name='basic_login'),
    path('login/', views.login, name='login'),
    path('basic_logout/', views.basic_logout, name='basic_logout'),
    path('logout/', views.logout, name='logout'),
    path('follow/<int:user_pk>', views.follow, name='follow'),
    path('mypage/<str:username>', views.mypage, name='mypage'),
    path('profile/<str:username>', views.profile, name='profile'),
]

