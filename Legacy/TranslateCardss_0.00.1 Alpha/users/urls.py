from django.urls import path, include
from main.views import index

from users.views import register, login

app_name = 'users'
urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
]