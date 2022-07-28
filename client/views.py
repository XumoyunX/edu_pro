from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm

#
def homepage(request):
    return render(request=request, template_name="main/index.html")

def profile(request):
    return render(request=request, template_name="main/index.html")

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'main/sign_in.html'
    success_url = reverse_lazy('index')

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'main/sign_up.html'
    success_url = reverse_lazy('sign_in')
