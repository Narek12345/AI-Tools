from django.shortcuts import render
from django.http import HttpResponse


def home_telegram_page(request):
	return render(request, 'telegram_app/home_telegram.html')


def connect_bot(request):
	return render(request, 'telegram_app/connect_bot.html')
