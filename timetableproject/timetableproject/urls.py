from django.contrib import admin
from django.urls import path
from timetable import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("edit/<int:pk>/", views.edit_task, name="edit"),
    path("delete/<int:pk>/", views.delete_task, name="delete"),
    path("confirm-delete/<int:pk>/", views.confirm_delete, name="confirm_delete"),
]
