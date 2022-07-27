from django.urls import path
from client.views import ClientRegistration, ClientLogin, clinet_logout

app_name = 'client'


urlpatterns = [
    path('registration/', ClientRegistration.as_view(), name='registration'),
    path('login/', ClientLogin.as_view(), name='login'),
    path("logout/", clinet_logout, name="logout"),
]

