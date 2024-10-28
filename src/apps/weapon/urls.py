from django.urls import path
from .views import list, show, add, update, deactivate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:weapon_id>', show, name='show'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('deactivate/<int:weapon_id>', deactivate, name='deactivate'),
    path('delete/<int:weapon_id>', delete, name='delete'),
]