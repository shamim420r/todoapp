from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import Tasks


def todo_list(request):
    context = {'todo_list': Tasks.objects.all()}
    return render(request, "Todo/todo_list.html", context)


def todo_view(request, id):
    context = {'todo_list': Tasks.objects.all().filter(id=id)}
    return render(request, "Todo/todo_view.html", context)


def todo_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TodoForm()
            form_class = todo_form
        else:
            todo = Tasks.objects.get(pk=id)
            form = TodoForm(instance=todo)
            form_class = todo_form
        return render(request, "Todo/todo_form.html", {'form': form})
    else:
        if id == 0:
            form = TodoForm(request.POST)
        else:
            todo = Tasks.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/todo/list')


def todo_delete(request, id):
    todo = Tasks.objects.get(pk=id)
    todo.delete()
    return redirect('/todo/list')
