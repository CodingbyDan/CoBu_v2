from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('home')