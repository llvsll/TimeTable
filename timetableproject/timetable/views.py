from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, DAYS
from .forms import TaskForm


def index(request):
    tasks_by_day = {}

    for key, label in DAYS:
        tasks = Task.objects.filter(day=key).order_by("time")
        tasks_by_day[label] = tasks

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(
        request,
        "index.html",
        {
            "form": form,
            "tasks_by_day": tasks_by_day,
        },
    )


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "edit.html", {"form": form})
