from django.urls import path
from  main.views import *


urlpatterns = [
    path('', index, name='index'),
    path('course/', course, name='course'),
    path('course_lesson/', course_lesson, name='course_lesson'),
    path('course_video/<int:id>/', course_video, name='course_video'),
    path('tulov/',tulov, name='tulov'),
    path('rayteng/', rayteng, name='rayteng'),
    path('our_team/', our_team, name='our_team'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('lesson/<int:id>/', lesson, name='lesson'),
]