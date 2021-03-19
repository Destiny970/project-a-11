from django.urls import path
from . import views

app_name = 'exercise'
urlpatterns = [   
    # path('', views.home, name='home'),
    path('', views.user_home, name='user_home'),
    # path('accounts/google/login/', views.user_home, name='user_home'),
    path('LogNW/', views.log_nws, name='log_new'),
    path('MyWorkouts/', views.my_ws, name='my_ws'),
    path('MyPoints/', views.my_points, name='my_points'),
]
