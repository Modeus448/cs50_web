from django.urls import path
from . import views

app_name = 'tasks' #дрдав імя додатка для уникнення конфлікту
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]
