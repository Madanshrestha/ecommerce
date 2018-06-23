from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.views.generic import FormView, View
from django.utils.http import is_safe_url

from .forms import RegisterForm, LoginForm

# Create your views here.


def login_page(request):

    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    print("User logged in")
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("home")
        else:
            print("error")
    return render(request, 'user_log.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'user_reg.html', context)
