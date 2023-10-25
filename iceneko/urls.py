from django.urls import path
from . import views

urlpatterns = [
    path('iceneko/', views.iceneko, name='iceneko'),
    path('menu/', views.menu, name='menu'),
]