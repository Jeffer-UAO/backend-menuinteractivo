from django.urls import path
from jump.views import index

urlpatterns = [
    path('', index),
]
