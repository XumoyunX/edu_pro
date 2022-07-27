from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, RegisterView
from . import views

app_name = "acounts"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("accounts/profile/", views.profile, name="profile"),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
