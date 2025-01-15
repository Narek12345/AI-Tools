from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(
				request,
				username=username,
				password=password,
			)
			if user is not None:
				login(request, user)
				return redirect('home')
	else:
		form = LoginForm()

	context = {'form': form}
	return render(request, 'account/login.html', context)
