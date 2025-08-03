from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"


class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    
    model = Project
    fields = (
        "title",
        "body",
    )
    template_name = "project_edit.html"


class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    
    model = Project
    template_name = "project_delete.html"
    success_url = reverse_lazy("project_list")


class ProjectCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Project
    template_name = "project_new.html"
    fields = (
        "title",
        "body",
    )
