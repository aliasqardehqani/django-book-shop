
from django.urls import path
from .views import HomePageView
from django.contrib.auth import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]