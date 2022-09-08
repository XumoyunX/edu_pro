from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import *
from .forms import *
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
    success_url = reverse_lazy('index')


def login_required_decorator(f):
    return login_required(f, login_url="client:login")


@login_required_decorator
def dashboard(request):
    return render(request=request, template_name = "dashboard/index.html")



def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client:dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('main:login')



def team_list(request):
    student = Team.objects.all()
    ctx = {
        'student':student,
        "c_active": 'active'
    }
    return render(request,'dashboard/team/list.html',ctx)




def team_create(request):
    model = Team()
    form = TeamForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:team_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)



def team_edit(request, pk):
    model = Team.objects.get(id=pk)
    form = TeamForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:team_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)




def team_delete(request, pk):
    model = Team.objects.get(id=pk)
    model.delete()
    return redirect('main:team_list')





def courses_list(request):
    course =Coueres.objects.all()
    ctx = {
        'course':course,
        "e_active": 'active'
    }
    return render(request,'dashboard/courses/list.html',ctx)




def courses_create(request):
    model = Coueres()
    form = CoueresForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/courses/form.html', ctx)



def courses_edit(request, pk):
    model = Coueres.objects.get(id=pk)
    form = CoueresForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:dashboard')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/courses/form.html', ctx)




def courses_delete(request, pk):
    model = Coueres.objects.get(id=pk)
    model.delete()
    return redirect('client:dashboard')




def talaba_list(request):
    student =Team_bola.objects.all()
    ctx = {
        'student':student,
        "e_active": 'active'
    }
    return render(request,'dashboard/natija/list.html',ctx)




def talaba_create(request):
    model = Team_bola()
    form = Team_bolaForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:talaba_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/natija/form.html', ctx)



def talaba_edit(request, pk):
    model = Team_bola.objects.get(id=pk)
    form = Team_bolaForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:talaba_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/natija/form.html', ctx)




def talaba_delete(request, pk):
    model = Team_bola.objects.get(id=pk)
    model.delete()
    return redirect('client:talaba_list')




def statistika_list(request):
    statictika =Statika.objects.all()
    ctx = {
        'statictika':statictika,
        "e_active": 'active'
    }
    return render(request,'dashboard/statistika/list.html',ctx)




def statistika_create(request):
    model = Statika()
    form = StatikaForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:statistika_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/statistika/form.html', ctx)



def statistika_edit(request, pk):
    model = Statika.objects.get(id=pk)
    form = StatikaForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:statistika_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/statistika/form.html', ctx)




def statistika_delete(request, pk):
    model = Statika.objects.get(id=pk)
    model.delete()
    return redirect('main:statistika_list')
