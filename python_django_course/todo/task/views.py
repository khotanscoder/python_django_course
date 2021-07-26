from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Task


# Create your views here.
# def maktabsample(request):
#     # if request.method == "POST":
#     #     print('hooooooraaaaaaaa')
#     #     print(dict(request.POST.items()))
#
#     tasks = Task.objects.all()
#     return render(request, 'maktab51.html', {'tasks': tasks})


class TaskListView(ListView):
    model = Task
    template_name = 'home-page.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task-detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task-new.html'
    fields = ['title', 'description']


