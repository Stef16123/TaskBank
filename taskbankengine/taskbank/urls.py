from django.urls import path, include
from .views import *


urlpatterns = [
	path('', TasksListView.as_view(), name="bank_list_url"),
	path('task/<str:slug>/', TaskDetailView.as_view(), name="task_detail_url"),

]