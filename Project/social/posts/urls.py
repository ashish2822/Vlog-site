from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('create/', views.posts_create, name='posts_create'),
    path('<int:post_id>/edit/', views.posts_edit, name='posts_edit'),
    path('<int:post_id>/delete/', views.posts_delete, name='posts_delete'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
] 