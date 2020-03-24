from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import Task


# Create your views here.

class TaskDetailView(DetailView):
	"""обработка списка задач. Сюда входят: получение полного списка и его ограничение"""
	model = Task
	template_name = 'taskbank/task_detail.html'


class TasksListView(ListView):
	"""Обработка одной конкретной задачи: """
	model = Task
	paginate_by = 2
	template_name = 'taskbank/index.html'
	context_object_name = 'tasks'
