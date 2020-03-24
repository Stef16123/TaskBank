from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.views.generic import View
from django.db.models import Q

from .models import Task


# Create your views here.

class TaskDetailView(DetailView):
	"""обработка списка задач. Сюда входят: получение полного списка и его ограничение"""
	model = Task
	template_name = 'taskbank/task_detail.html'


class TasksListView(View):
	"""Обработка одной конкретной задачи: """

	model = Task
	template_name = 'taskbank/index.html'

	def get(self,request):
		search_query = request.GET.get('search', '')
		if search_query:
			task = self.model.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
		else:
			task = self.model.objects.all()

		paginator = Paginator(task, 2)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)
		context = {
		'tasks' : page,
		}
		return render(request, self.template_name, context)
