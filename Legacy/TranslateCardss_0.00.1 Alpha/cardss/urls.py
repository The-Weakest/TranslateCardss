from django.urls import path, include
from main.views import index

from users.views import cardsview, cardssmakes

app_name = 'users'
urlpatterns = [
    path('cardssview', cardssview, name="login"),
    path('cardssmakes', cardssmakes, name="register"),
]