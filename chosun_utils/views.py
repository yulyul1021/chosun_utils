from django.shortcuts import render, redirect, get_object_or_404
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


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('')


def delete_scrap(request, scrap_id):
    scrap = get_object_or_404(Scrap, pk=scrap_id)
    scrap.delete()
    return redirect('')


def calendar(request):
    return render(request, 'chosun_utils/chosun_calendar.html')


def notice(request):
    return render(request, 'chosun_utils/chosun_notice.html')


def language(request):
    return render(request, 'chosun_utils/chosun_language.html')


def scholarship(request):
    return render(request, 'chosun_utils/chosun_scholarship.html')


def ctl(request):
    return render(request, 'chosun_utils/chosun_ctl.html')


def program(request):
    return render(request, 'chosun_utils/chosun_program.html')


def work(request):
    return render(request, 'chosun_utils/extra_work.html')


def sidejob(request):
    return render(request, 'chosun_utils/extra_sidejob.html')


def campuspick(request):
    return render(request, 'chosun_utils/extra_campuspick.html')


def competition(request):
    return render(request, 'chosun_utils/extra_competition.html')


def gjyouth(request):
    return render(request, 'chosun_utils/extra_gjyouth.html')
