from django.shortcuts import render, redirect
from .models import Todo, Scrap
from .forms import TodoForm, ScrapForm


def index(request):
    todo_form = TodoForm()
    scrap_form = ScrapForm()

    if request.method == 'POST':
        if 'todo_submit' in request.POST:
            todo_form = TodoForm(request.POST)
            if todo_form.is_valid():
                todo_form.save()
        elif 'scrap_submit' in request.POST:
            scrap_form = ScrapForm(request.POST)
            if scrap_form.is_valid():
                scrap_form.save()

    todos = Todo.objects.all()
    scraps = Scrap.objects.all()

    return render(request, 'chosun_utils/mypage.html', {
        'todo_form': todo_form,
        'scrap_form': scrap_form,
        'todos': todos,
        'scraps': scraps,
    })
