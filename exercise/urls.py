from django.urls import path
from . import views
# from .views import list_posts, new_post
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
app_name = 'exercise'
urlpatterns = [   
    path('', views.home, name='home'),
    path('UserHome/', views.user_home, name='user_home'),
    path('', views.index, name='index'),
    path('LogNW/', views.log_nws, name='log_new'),
    path('MyWorkouts/', views.my_ws, name='my_ws'),
    path('MyPoints/', views.my_points, name='my_points'),

    # Added 03/19/21
    # path('visibility/', list_posts, name='public_private'),
    # path('new/', new_post, name='new_post'),
    # path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
