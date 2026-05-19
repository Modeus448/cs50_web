from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #створюємо форму для додавання нових завдань
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=4) #додаємо поле для пріоритету завдання

def index(request):
    return render(request, 'tasks/index.html', 
        {"tasks": tasks})
def add(request):
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()})

# Create your views here.
