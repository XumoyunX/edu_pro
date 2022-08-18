from django.contrib import admin
from django.urls import path
from client.views import LoginView, RegisterView
from . import views

app_name = "client"

urlpatterns = [
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path("", views.homepage, name="homepage"),
    path("accounts/profile/", views.profile, name="profile"),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('team_list/', views.team_list, name="team_list"),
    path('team_create/', views.team_create, name="team_create"),
    path('<int:pk>/team_edit/', views.team_edit, name="team_edit"),
    path('<int:pk>/team_delete/', views.team_delete, name="team_delete"),

    path('courses_list/', views.courses_list, name="courses_list"),
    path('courses_create/', views.courses_create, name="courses_create"),
    path('<int:pk>/courses_edit/', views.courses_edit, name="courses_edit"),
    path('<int:pk>/courses_delete/', views.courses_delete, name="courses_delete"),

    path('talaba_list/', views.talaba_list, name="talaba_list"),
    path('talaba_create/', views.talaba_create, name="talaba_create"),
    path('<int:pk>talaba_edit/', views.talaba_edit, name="talaba_edit"),
    path('<int:pk>/talaba_delete/', views.talaba_delete, name="talaba_delete"),

    path('statistika_list/', views.statistika_list, name="statistika_list"),
    path('statistika_create/', views.statistika_create, name="statistika_create"),
    path('<int:pk>/statistika_edit/', views.statistika_edit, name="statistika_edit"),
    path('<int:pk>/statistika_delete/', views.statistika_delete, name="statistika_delete"),
]
