from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.generic import FormView, View
from .forms import RegisterForm, LoginForm

# Create your views here.

class RegisterView(FormView):
    template_name = "user_reg.html"

    def get(self, request):
        form = RegisterForm()
    
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password2'])
            user.save()

            return redirect("user_login")

        return redirect("user_register")

class LoginView(FormView):
    template_name = "user_log.html"

    def get(self, request):
        form = LoginForm()

        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)

            if not auth_user:
                error_message = "Username or Password didn't match"
                form = LoginForm()
                return render(request, self.template_name, {'form':form, 'error_message':error_message})

            auth_login(request, auth_user)
            return redirect('home')

class LogoutView(View):
    
    def get(self, request):
        auth_logout(request)
        return redirect("user_login")
