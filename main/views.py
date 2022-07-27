from django.shortcuts import render
from main.models import *

def index(requesrt):
    statictika=Statika.objects.all()

    ctx={
        "statictika":statictika

    }
    return render(requesrt, 'main/index.html',ctx)


def course(requesrt):
    return render(requesrt, 'main/kurslar.html')


def course_lesson(request):
    return render(request, 'main/kurs_dars.html')


def rayteng(request):
    student = Team_bola.objects.all()

    ctx={
        "student":student
    }
    return render(request, 'main/natija.html',ctx)


def our_team(request):
    student=Team.objects.all()

    ctx={
        "student":student
    }

    return render(request, 'main/biz_jamo.html',ctx)


def sign_up(request):
    return render(request, 'main/sign_up.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def lesson(request):
    return render(request, 'main/dars.html')



def hello(request):
    pass


