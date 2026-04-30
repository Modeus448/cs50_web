#Таблиця URL-адрес для проекту Django. 
#Вона визначає, які URL-адреси будуть оброблятися якими функціями або класами у вашому додатку. 
#Также тута портібно прописувати add urls для корккної роботи
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")),
    path("newyear/", include("newyear.urls")),
]
