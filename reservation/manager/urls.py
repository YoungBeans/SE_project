
from django.urls import path
from . import views

urlpatterns = [
    path('', views.m_home, name='m_home'),
    path('accept/managing/', views.m_accept, name='m_accept'),
]
