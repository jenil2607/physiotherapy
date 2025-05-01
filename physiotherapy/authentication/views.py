from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth's user creation 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
from authentication.forms import CustomUserRegisterForm


# Create your views here.

class UserRegister(CreateView):
    form_class = UserCreationForm # spacefaying hte way 
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

class Login(LoginView):
    template_name = 'login.html'

# authentication/views.py
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        print("Form is valid ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid ❌")
        print(form.errors)
        return super().form_invalid(form)


class UserRegister(CreateView):
    form_class = CustomUserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

def forgot_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successful. You can now log in.')
            return redirect('signin')  # or wherever your login page is
        except User.DoesNotExist:
            messages.error(request, 'Username not found.')

    return render(request, 'authentication/forgot_password.html')