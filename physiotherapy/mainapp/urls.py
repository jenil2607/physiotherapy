from django.urls import path
from .views import home, book_appointment, appointment_list
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Home page
    # path('book/', book_appointment, name='book_appointment'),  # Book appointment
    # path('appointments/', appointment_list, name='appointment_list'),  # View appointments

    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]

