from django.urls import path

from tasks.views import (TagsListView, TagCreateView, TagUpdateView,
                         TagDeleteView, TaskListView, TaskCreateView,
                         TaskToggleView, TaskUpdateView, TaskDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/edit/", TagUpdateView.as_view(), name="tag-edit"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task-edit"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),

]

app_name = 'task'
