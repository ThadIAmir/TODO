from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
    UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from base.models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(CustomLoginView, self).get(*args, **kwargs)


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user = self.request.user)
        context['counts'] = context['tasks'].filter(complete=False).count()

        q = self.request.GET.get('q') or ''
        context['tasks'] = context['tasks'].filter(
            Q(title__icontains=q) | Q(description__icontains=q))
        context['q'] = q

        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail.html'

    def get_object(self, queryset=None):
        """
        Override get_object to ensure only the task owner can update the task.
        """
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this task.")  # Raises 403 Forbidden
        return task

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'base/task_update.html'
    success_url = reverse_lazy('tasks')

    def get_object(self, queryset=None):
        """
        Override get_object to ensure only the task owner can update the task.
        """
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this task.")  # Raises 403 Forbidden
        return task


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')

    def get_object(self, queryset=None):
        """
        Override get_object to ensure only the task owner can access or delete the task.
        """
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise Http404  # Return a 404 if the user is not the owner
        return task




