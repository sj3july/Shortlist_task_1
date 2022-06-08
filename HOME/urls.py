from django.contrib import admin
from django.urls import path
from HOME import views
urlpatterns = [
    
    path("", views.index,name="HOME"),
    path("for_doctor", views.for_doctor,name="for_doctor"),
    path("for_patient", views.for_patient,name="for_patient"),
    path("services", views.services,name="services"),
    path("about", views.about,name="about"),
    path("contact", views.contact,name="contact"),
]
