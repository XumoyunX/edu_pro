from django.shortcuts import render
from main.models import *


def index(requesrt):
    statictika = Statika.objects.all()
    bizningjamoa = Team.objects.all()
    course = Coueres.objects.all()
    lesson = Coueres.objects.all()
    ctx = {
        "lesson": lesson,
        "course": course,
        "bizningjamoa": bizningjamoa,
        "statictika": statictika

    }
    return render(requesrt, 'main/index.html', ctx)


def course(requesrt):
    course = Coueres.objects.all()

    ctx = {
        "course": course
    }
    return render(requesrt, 'main/kurslar.html', ctx)


def course_lesson(request):
    lesson = Coueres.objects.all()

    ctx = {
        "lesson": lesson
    }
    return render(request, 'main/kurs_dars.html', ctx)


def course_video(request, id):
    vedio = Coueres.objects.filter(id=id)
    ctx = {
        "vedio": vedio
    }
    return render(request, 'main/dars.html', ctx)


def rayteng(request):
    student = Team_bola.objects.all()

    ctx = {
        "student": student
    }
    return render(request, 'main/natija.html', ctx)


def tulov(request):
    return render(request, "main/to'lov.html")


def our_team(request):
    student = Team.objects.all()

    ctx = {
        "student": student
    }

    return render(request, 'main/biz_jamo.html', ctx)


def sign_up(request):
    return render(request, 'main/sign_up.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def lesson(request):
    return render(request, 'main/dars.html')


def hello(request):
    pass
