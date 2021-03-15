from django.contrib import admin
# importing urls for allauth and TemplateView (03/01/21)
from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'exercise'
urlpatterns = [
    # added 03/01/21
    path('', TemplateView.as_view(template_name = "exercise/index.html")),
    # added 03/01/21
    path('accounts/', include('allauth.urls'))
    
    path('exercise/', include('exercise.urls')),
    path('admin/', admin.site.urls),
]
