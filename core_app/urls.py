from django.urls import path

from core_app import views


urlpatterns = [
	path('', views.home_page, name='home'),
]
