from django.shortcuts import render


def index(requesrt):
    return render(requesrt, 'main/index.html')


def course(requesrt):
    return render(requesrt, 'main/kurslar.html')


def course_lesson(request):
    return render(request, 'main/kurs_dars.html')


def rayteng(request):
    return render(request, 'main/natija.html')


def our_team(request):
    return render(request, 'main/biz_jamo.html')


def sign_up(request):
    return render(request, 'main/sign_up.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def lesson(request):
    return render(request, 'main/dars.html')
