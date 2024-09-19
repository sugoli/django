from django.urls import path
from myauth import views

app_name = 'myauth'

urlpatterns = [
    path('register/', views.register,name = 'register'),
    path('login/',views.user_login,name = 'user_login'),
]