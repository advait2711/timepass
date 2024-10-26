from django.urls import path
from home.views import *

path('', home, name = 'home'), 
path('resume/', gen_resume, name = 'resume'),