from django.urls import path
from .views import *


urlpatterns = [
   path('',homepage , name=''),
   path('register/',register , name='register'),
   path('my_login/',my_login , name='my_login'),
   path('dashboard/',dashboard , name='dashboard'),
]
