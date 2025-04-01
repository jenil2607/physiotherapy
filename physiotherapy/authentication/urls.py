from django.urls import path
from. import views

urlpatterns = [
    path('login/',views.Login.as_view(), name = 'signin'),
    path('regiter/',views.UserRegister.as_view(), name = 'signup')

]