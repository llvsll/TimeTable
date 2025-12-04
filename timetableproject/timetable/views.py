from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, DAYS
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all().order_by("day", "time")

    DAYS_ORDERED = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П’ятниця",
        "Субота",
        "Неділя",
    ]

    calendar = {day: [] for day in DAYS_ORDERED}

    for task in tasks:
        if task.day in calendar:
            calendar[task.day].append(task)
        else:
            calendar.setdefault("Невідомо", []).append(task)

    form = TaskForm()

    return render(request, "index.html", {"form": form, "calendar": calendar})


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "edit.html", {"form": form})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "confirm_delete.html", {"task": task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")
