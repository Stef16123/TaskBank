from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Task


# Create your views here.
def bank_list(request):
	"""обработка списка задач"""
	tasks = Task.objects.all()
	paginator = Paginator(tasks, 2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	context = {
	'tasks' : page,
	}
	return render(request,'taskbank/index.html', context)

def task_detail(request, slug):
	"""Обработка одной конкретной задачи"""
	task = Task.objects.get(slug__iexact=slug)
	context = {'task' : task, 'slug' : slug}
	return render(request, 'taskbank/task_detail.html', context)