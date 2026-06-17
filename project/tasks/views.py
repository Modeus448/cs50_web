from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #створюємо форму для додавання нових завдань
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=4) #додаємо поле для пріоритету завдання

def index(request):
    return render(request, 'tasks/index.html', 
        {"tasks": tasks})

def add(request):
    #Перевірка на сервері
    if request.method == "POST":
        form = NewTaskForm(request.POST) #створюємо екземпляр форми з даними, отриманими від користувача
        if form.is_valid(): #перевіряємо, чи дані є валідними
            task = form.cleaned_data #отримуємо дані з форми
            tasks.append(task) #додаємо нове завдання до списку завдань
            return HttpResponseRedirect(reverse("tasks:index")) #перенаправляємо користувача на головну сторінку
        else:
            return render(request, "tasks/add.html", {
                "form": form}) #якщо дані не є валідними, повертаємо форму з помилками для виправлення користувачем
#просто рендеремо сторінку
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()})

# Create your views here.
