#Обираємо що баче користувач, який зайшов на сайт
from django.shortcuts import render

def index(request): #request -це запит користувача, який зайшов на сайт
    return render(request, 'index.html') #render - це функція, яка повертає HTML сторінку,
            #яку ми хочемо показати користувачу. 'index.html' - це назва файлу, який ми хочемо показати користувачу.

