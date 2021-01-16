from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Todo

# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todos'



class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'



class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = '__all__'



class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    fields = ['deadline']
