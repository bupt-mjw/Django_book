from django.urls import path, include
from book.views import index

urlpatterns = [
    path('index/', index),
]