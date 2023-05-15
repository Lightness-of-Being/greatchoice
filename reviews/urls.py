from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_type>', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('detail/<int:product_pk>', views.detail, name='detail'),
    path('product_create/', views.product_create, name='product_create'),
    path('detail/<int:product_pk>/review_create/', views.review_create, name='review_create'),
    path('detail/<int:product_pk>/delete/', views.product_delete, name='product_delete'),
    path('detail/<int:product_pk>/delete/<int:review_pk>/', views.product_delete, name='review_delete'),
    path('update/<int:product_pk>/', views.product_update, name='product_update'),
    path('detail/<int:product_pk>/update/<int:review_pk>/', views.review_update, name='review_update'),
]
