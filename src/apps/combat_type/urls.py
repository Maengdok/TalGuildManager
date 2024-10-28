from django.urls import path
from .views import list, show, add, update, deactivate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:combat_type_id>', show, name='show'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('deactivate/<int:combat_type_id>', deactivate, name='deactivate'),
    path('delete/<int:combat_type_id>', delete, name='delete'),
]