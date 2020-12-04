from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('signout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
]