from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>', views.ProfileView.as_view(), name='profile_detail'),
    
    
    path('login/', 
         
         LoginView.as_view(template_name='users/login.html', 
            redirect_authenticated_user=True, next_page='post'),
         
         name='login'
         ),
    path('logout/', LogoutView.as_view(next_page='post'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]