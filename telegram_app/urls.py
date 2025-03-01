from django.urls import path

from telegram_app import views


app_name = "telegram_app"

urlpatterns = [
	path('', views.home_telegram_page, name="home_telegram"),
	path('connect-bot', views.connect_bot, name="connect_bot"),
	path('bot/<int:bot_id>', views.show_bot, name='show_bot'),
	path('bot/start/<int:bot_id>', views.start_bot, name='start_bot'),
]
