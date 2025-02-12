from django.shortcuts import render


def home_telegram_page(request):
	return render(request, 'telegram_app/home_telegram.html')
