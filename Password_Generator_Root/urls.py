from django.urls import path
from Generator import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('password', views.password, name='password'),
]
