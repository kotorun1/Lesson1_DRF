"""Merzlyakov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('',views.apiOverview, name="api-overview"),
        path('books-list/',views.booksList, name="books-list"),
        path('book-detail/<str:pk>/',views.bookDetail, name="book-detail"),
        path('book-create/',views.bookCreate, name="book-create"),
        path('book-update/<str:pk>/',views.bookUpdate, name="book-update"),
        path('book-delete/<str:pk>/',views.bookDelete, name="book-delete"),

]
