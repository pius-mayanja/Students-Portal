from django.urls import path
from .views import home

app_name = 'user'

urlpatterns = [
    path('', home, name='home'),
]