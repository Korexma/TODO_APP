from django.urls import path

from .views import TodoCreateView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/new', TodoCreateView.as_view(), name='todo_new'),
    #path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit')
]
