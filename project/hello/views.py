#Обираємо що баче користувач, який зайшов на сайт
#Тута ми прописуємо файли які будуть показані і їхні назви в коді 
from django.shortcuts import render
from django.http import HttpResponse

def index(request): #request -це запит користувача, який зайшов на сайт
    return render(request, 'hello/index.html') #render - це функція, яка редерить на запити щось,
        #return HttpResponse("Hello, world!")            
        #яку ми хочемо показати користувачу. 'index.html' - це назва файлу, який ми хочемо показати користувачу.

def names(request):
#Функція назва функції (запит)
    return HttpResponse("My name is Bohdan")
    #вивести на екран текст "My name is Bohdan"


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()}) #Додаємо до html логіку, шаблоназацію і додаємо зміну
    #вивести на екран текст "Hello, {name}!", де {name} - це ім'я, яке ми передаємо в URL-адресі.
