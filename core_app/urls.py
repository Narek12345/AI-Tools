from django.urls import path

from core_app import views


app_name = 'core_app'

urlpatterns = [
	path('', views.home_page, name='home'),
	path('no_function', views.no_function, name="no_function"),
]
