from django.db import models

# Create your models here.


class Task(models.Model):
	"""Модель для задачи, имеет название, текстовую запись и слаг, и время добавления"""
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, unique=True)
	body = models.TextField(blank=True)
	date_pub = models.DateTimeField(auto_now_add=True)

	class Meta:
		#Переобъявить порядок сортировки по убыванию
		ordering = ['-date_pub'] 

	def __str__(self):
		return self.title
