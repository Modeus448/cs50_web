#Обираємо що баче користувач, який зайшов на сайт
from django.shortcuts import render
from django.http import HttpResponse

def index(request): #request -це запит користувача, який зайшов на сайт
         #return render(request), 'index.html') #render - це функція, яка приймає запит користувача і назву шаблону,
    return HttpResponse("Hello, world!")            
        #яку ми хочемо показати користувачу. 'index.html' - це назва файлу, який ми хочемо показати користувачу.

