from django.urls import path
from .views import home, book_appointment, appointment_list, review_page, therapy_session_list, create_therapy_session, Admin_Dashboard
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('reviews/', review_page, name='review_page'),
    path('admin/dashboard/', Admin_Dashboard.as_view(), name='admin_dashboard'),
    path('therapy-sessions/', therapy_session_list, name='therapy_session_list'),
    path('therapy-sessions/new/', views.create_therapy_session, name='create_therapy_session'),

]

