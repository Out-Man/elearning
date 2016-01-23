from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from .forms import LoginForm, RegisterForm
from .models import MyUser
from django.core.urlresolvers import reverse

from notifications.models import Notification
from billing.models import Transaction


@login_required
def account_home(request):
	notifications = Notification.objects.get_recent_for_user(request.user, 6)
	transactions = Transaction.objects.get_recent_for_user(request.user, 3)
	context = {
		"notifications": notifications,
		"transactions": transactions
	}

	return render(request, "accounts/account_home.html", context)

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			if next_url:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect('/')

	action_url = action_url = reverse('auth_login')
	title = 'Login'
	submit_btn = title
	submit_btn_class = "btn-success btn-block"
	extra_form_link = "Upgrade your account today <a href='%s'>here</a>!" %(reverse("account_upgrade"))

	template = 'accounts/account_login_register.html'
	context = {
		'form': form,
		'action_url': action_url,
		'title': title,
		'submit_btn': submit_btn,
		"submit_btn_class": submit_btn_class,
		"extra_form_link":extra_form_link
	}
	return render(request, template, context)

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


def auth_register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		#MyUser.objects.create_user(username=username, email=email, password=password)
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		#new_user.password = password #WRONG
		new_user.set_password(password) #RIGHT set_password changes password to a hashed password.
		new_user.save()

	action_url = reverse("register")
	title = "Register"
	submit_btn = "Create free account"
	submit_btn_class = "btn-success btn-block"

	context = {
		"form": form,
		"action_url": action_url,
		"title": title,
		"submit_btn": submit_btn,
		"submit_btn_class": submit_btn_class
		}
	return render(request, 'accounts/account_login_register.html', context)