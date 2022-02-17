
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
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
    

    
class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'users/edit-profile.html'
    fields= ['name', 'username', 'email', 'bio', 'profile_image']
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    
class FollowView(View):
    
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['pk'])
        current_profile = Profile.objects.get(id=request.user.profile.id)
        following = profile.following.all()
        
        if kwargs['pk'] != current_profile.id:
            if current_profile in following:
                profile.following.remove(current_profile.id)
                
            else:
                profile.following.add(current_profile.id)
                
                
                
        return redirect(reverse('profile_detail', kwargs={"pk":profile.id}))
        
    