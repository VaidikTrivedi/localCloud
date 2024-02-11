from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logoutView, name='logout'),
    path('register/afterLogin/',views.afterLogin, name='afterLogin')
]