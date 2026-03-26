from django.urls import path
from core.views.base import index

urlpatterns = [
    path('', index, name='index'),
]