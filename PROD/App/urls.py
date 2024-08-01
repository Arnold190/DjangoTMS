from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import CustomLoginView



urlpatterns = [
path('', CustomLoginView.as_view(), name='login'),
#path('logout/', auth_views.login, name='logout'),
#path('info/', views.info, name='info'),

]