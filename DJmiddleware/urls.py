from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exp/', views.Exp),
    path('name/', views.name),
]
