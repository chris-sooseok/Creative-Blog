import os
import pathlib
from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryDeleteFunction, CategoryUpdateView, NoteDeleteFunction, NoteUpdateFunction, NoteCreateFunction, TopicUpdateView, TopicDeleteFunction, TopicDetailView, TopicCreateView , TopicListView, NoteDetailFunction

urlpatterns = [
    path('', CategoryListView.as_view(), name=os.path.basename(pathlib.Path(__file__).parent.resolve())),
    path('create_category/', CategoryCreateView.as_view(), name="create_category"),
    path('delete_category/<uuid:pk>', CategoryDeleteFunction, name="delete_category"),
    path('update_category/<uuid:pk>', CategoryUpdateView.as_view(), name="update_category"),
    path('<uuid:pk>', CategoryDetailView.as_view(), name="category_detail"),
    path('list_topic', TopicListView.as_view(), name="list_topic"),
    path('create_topic/<uuid:pk>', TopicCreateView.as_view(), name="create_topic"),
    path('delete_topic/<uuid:pk>', TopicDeleteFunction, name="delete_topic"),
    path('update_topic/<uuid:pk>', TopicUpdateView.as_view(), name="update_topic"),
    path('<uuid:pk>/', TopicDetailView.as_view(), name="topic_detail"),

    path('create_note/<uuid:pk>', NoteCreateFunction, name="create_note"),
    path('<uuid:topic_pk>/<uuid:note_pk>', NoteDetailFunction, name="note_detail"),
    path('update_note/<uuid:topic_pk>/<uuid:note_pk>', NoteUpdateFunction, name="update_note"),
    path('delete_note/<uuid:topic_pk>/<uuid:note_pk>', NoteDeleteFunction, name="delete_note"),
    #path('clean_file/', FileCleanFunction, name='clean_file'),
]