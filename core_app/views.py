from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
	"""Представление домашней страницы."""
	return render(request, 'core_app/home.html')


def no_function(request):
	return render(request, 'core_app/no_function.html')
