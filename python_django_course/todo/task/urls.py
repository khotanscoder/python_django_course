from django.urls import path
from .views import TaskCreateView, TaskDetailView, TaskListView

urlpatterns = [
    # path('maktab51/', maktabsample),
    path('new/', TaskCreateView.as_view(), name='new-task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('', TaskListView.as_view(), name='home'),

]
