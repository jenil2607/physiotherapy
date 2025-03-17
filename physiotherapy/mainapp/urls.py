from django.urls import path
from .views import home, book_appointment, appointment_list, progress_report, user_login, user_signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('book/', book_appointment, name='book_appointment'),  # Book appointment
    path('appointments/', appointment_list, name='appointment_list'),  # View appointments
    path('progress/', progress_report, name='progress_report'),  # Progress report
    path('login/', user_login, name='login'),  # Login page
    path('signup/', user_signup, name='signup'),  # Signup page
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout
]

