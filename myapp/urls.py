from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy

urlpatterns = [
    path('Items/',ItemListCreate.as_view(), name='Item-list-create'),
    path('Items/<int:pk>/',ItemRetrieveUpdateDestroy.as_view(), name='Item-retrieve-update-destroy'),
]