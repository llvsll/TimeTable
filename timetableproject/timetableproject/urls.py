from django.contrib import admin
from django.urls import path
from timetable import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("edit/<int:pk>/", views.edit_task, name="edit"),
]
