from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.upload_file, name = 'upload_file'),
    path('filelist/', views.file_list, name= 'file_list'),
    path('register/', views.user_register, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
