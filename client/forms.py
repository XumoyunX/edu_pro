from django import forms
from client.models import User
from django.core.exceptions import ValidationError








class RegistrationForm(forms.ModelForm):

    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label=('Parol takroran'))

    def clean_fields(self):
        if self.cleaned_data["confirm"] != self.cleaned_data["password"]:
            raise ValidationError("Parollar bir xil bo'lish kerak !")

        return self.cleaned_data['confirm']



    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username": ('Login'),
            "password": ('Parol')

        }

        help_texts = {
            "username": ("Lotin harflari, sonlar va @/#/$/%/^/&/_ belgilar iborat bo'lish lozim")
        }

        widgets = {
            'password': forms.PasswordInput
        }




class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=('Login'), required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label=('Parol'),  required=True)



#
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
# from django import forms
#
#
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username', 'password1', 'password2')
#
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Email / Username')