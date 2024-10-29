from django.urls import path
from .views import list, show, add, update, deactivate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:member_id>', show, name='show'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('deactivate/<int:member_id>', deactivate, name='deactivate'),
    path('delete/<int:member_id>', delete, name='delete'),
]