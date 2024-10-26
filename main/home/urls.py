# home/urls.py

from django.urls import path
from home.views import home, gen_resume  # Import your views

urlpatterns = [
    path('', home, name='home'),          # URL for the home page
    path('resume/', gen_resume, name='resume'),  # URL for the resume generation
]
