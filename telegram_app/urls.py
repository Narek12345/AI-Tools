from django.urls import path

from telegram_app import views


app_name = "telegram_app"

urlpatterns = [
	path('', views.home_telegram_page, name="home_telegram"),
	path('connect-bot', views.connect_bot, name="connect_bot"),
]
