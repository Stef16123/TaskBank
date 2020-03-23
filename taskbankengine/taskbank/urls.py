from django.urls import path, include
from .views import *


urlpatterns = [
	path('', bank_list, name="bank_list_url"),
	path('<str:slug>/', task_detail, name="task_detail_url")
]