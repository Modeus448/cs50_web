import datetime
from django.shortcuts import render

def index(request):
    now = datetime.datetime.now() #Створуємо зміну для дати
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1 }), 
            #получаємо місять і порівнуємо і получаємо день і порівнуєм її 
