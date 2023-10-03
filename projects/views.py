from django.shortcuts import render, redirect
from .forms import AddProjectForm
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "home.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)


def add_project(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            technology = form.cleaned_data["technology"]
            # Project.objects.create(title=title, description=description, technology=technology)
            return redirect("")
    else:
        form = AddProjectForm()

    return render(request, "add_project.html", {"form": form})
