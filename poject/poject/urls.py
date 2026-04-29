#Таблиця URL-адрес для проекту Django. 
#Вона визначає, які URL-адреси будуть оброблятися якими функціями або класами у вашому додатку. 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")), #Посилання на додаток hello
]
