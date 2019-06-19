
from django.contrib import admin
from django.urls import path
from pages.views import home, contact, about, member,team,categoryWiseMember,greatmember


urlpatterns = [
    path('',home),
    path('members/', team, name="team"),
    path('member/<int:id>', member,name="member"),
    path('category/<int:cat_id>/member/<int:mem_id>', categoryWiseMember,name="categoryWiseMember"),
    path('contact/', contact.as_view()),
    path('about/', about),
    path('greatmember/', greatmember, name="greatmember"),

]
