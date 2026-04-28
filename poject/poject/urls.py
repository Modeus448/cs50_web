#Таблиця URL-адрес для проекту Django. 
#Вона визначає, які URL-адреси будуть оброблятися якими функціями або класами у вашому додатку. 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
