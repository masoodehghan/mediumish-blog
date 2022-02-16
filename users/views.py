from django.shortcuts import redirect, render
from django.views.generic import FormView, DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Profile

class RegisterView(FormView):
    
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = 'post'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(self.request, user)
        
        return redirect('post')

class ProfileView(DetailView):
    template_name = 'users/account.html'
    model = Profile
    context_object_name = 'user'