from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.models import Tag


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
