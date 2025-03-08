from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskFormUpdate, TaskFormCreate
from tasks.models import Tag, Task


class TagsListView(ListView):
    model = Tag
    template_name = 'tasks/tags_list.html'
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('task:tag-list')


class TagUpdateView(UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('task:tag-list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tasks/tag_delete.html'
    success_url = reverse_lazy('task:tag-list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskFormCreate
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task:task-list')


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = "tasks"
    ordering = ['is_done', '-deadline', '-created_at']


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse_lazy('task:task-list'))


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskFormUpdate
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task:task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task:task-list')