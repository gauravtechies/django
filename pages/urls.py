
from django.contrib import admin
from django.urls import path
from pages.views import home, contact, about


urlpatterns = [
    path('',home),
    path('contact/', contact.as_view()),
    path('about/', about),

]
