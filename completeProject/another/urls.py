from django.urls import path 
from .views import *


urlpatterns = [

    path('addtask/',addtask , name='addtask'),
]
