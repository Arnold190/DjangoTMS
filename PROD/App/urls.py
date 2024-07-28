from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
path('', views.login, name='login'),
#path('info/', views.info, name='info'),

]