from django.urls import path
from .views import list 

urlpatterns = [
    path('', list, name='list'),
]