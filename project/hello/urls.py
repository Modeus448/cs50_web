#Тута ми прописуємо їхні адреси для того щоб користувачі могли переходити на різні сторінки нашого сайту.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),#Посилання на головну сторінку
    path("names", views.names, name="names"),
    #("назва в посилані", views.назва функції, name="назва в коді")
    path("<str:name>", views.greet, name="greet")
    #("<str:name>" - це змінна, яка буде передаватися в функцію greet. 
    # Вона може бути будь-яким рядком, який ми передаємо в URL-адресі.
]
