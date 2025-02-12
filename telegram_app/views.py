from django.shortcuts import render
from django.http import HttpResponse


def home_telegram_page(request):
	return render(request, 'telegram_app/home_telegram.html')


def connect_telegram_bot(request):
	return render(request, 'telegram_app/connect_telegram_bot.html')
