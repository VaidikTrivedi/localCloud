from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name='logout')
]