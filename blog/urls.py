from django.urls import path
from . import views
from .views import UserPostListView,PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog_delete'),
    path('post/new/', PostCreateView.as_view(), name='blog_create'),
    path('about/', views.about, name='blog_about'),
]