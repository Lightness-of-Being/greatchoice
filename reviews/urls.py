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
from django.conf import settings
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('detail/<int:product_pk>', views.detail, name='detail'),
    path('product_create/', views.product_create, name='product_create'),
    path('detail/<int:product_pk>/review_create/', views.review_create, name='review_create'),
    path('detail/<int:product_pk>/delete/', views.product_delete, name='product_delete'),
    path('detail/<int:product_pk>/delete/<int:review_pk>/', views.product_delete, name='review_delete'),
    path('update/<int:product_pk>/', views.product_update, name='product_update'),
    path('detail/<int:product_pk>/update/<int:review_pk>/', views.review_update, name='review_update'),
]
