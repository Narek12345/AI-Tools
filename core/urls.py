from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('list_projects', views.list_projects, name='list_projects'),
]
