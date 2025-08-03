from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from .models import Project
from .forms import CommentForm


class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"


class CommentGet(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Project
    form_class = CommentForm
    template_name = "project_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.project = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        project = self.object
        return reverse("project_detail", kwargs={"pk": project.pk})

class ProjectDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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
