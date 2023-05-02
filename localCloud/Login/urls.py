from django.urls import path
from . import views

urlpatterns = [
    path('loginOld/', views.login, name='login'),
]