from django.urls import path
from . import views

app_name = 'exercise'
urlpatterns = [   
    path('', views.home, name='home'),
    path('UserHome/', views.user_home, name='user_home'),
    path('', views.index, name='index'),
    path('LogNW/', views.log_nws, name='log_new'),
    path('MyWorkouts/', views.my_ws, name='my_ws'),
    path('MyPoints/', views.my_points, name='my_points'),
    # path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

]

