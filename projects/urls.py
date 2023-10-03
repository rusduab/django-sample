from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("add", views.add_project, name="add_project"),
]