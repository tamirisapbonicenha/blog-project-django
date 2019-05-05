from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/', views.posts, name='posts'),
    path('posts/search/', views.search_posts, name='search_posts'),
    path('create', views.post_new, name='post_create'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
    # path('category_create/', views.category_create, name='category_create'),
]