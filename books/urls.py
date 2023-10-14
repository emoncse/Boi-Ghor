from django.contrib import admin
from django.urls import path, include
from books import views


urlpatterns = [
    path('<str:book_id>', views.home, name='home'),
]
