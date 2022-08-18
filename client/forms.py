from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from main.models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team()
        fields = '__all__'

class CoueresForm(forms.ModelForm):
	class Meta:
		model = Coueres()
		fields = "__all__"



class Team_bolaForm(forms.ModelForm):
	class Meta:
		model = Team_bola()
		fields = "__all__"


class StatikaForm(forms.ModelForm):
	class Meta:
		model = Statika()
		fields = "__all__"