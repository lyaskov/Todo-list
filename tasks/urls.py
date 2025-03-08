from django.urls import path

from tasks.views import TagsListView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/edit/", TagUpdateView.as_view(), name="tag-edit"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = 'task'
