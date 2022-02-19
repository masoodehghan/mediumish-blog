from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.ProfileView.as_view(), name='profile_detail'),
    path("profile/edit/<str:pk>", views.ProfileEditView.as_view(), name="profile_edit"),
    path("follow/<str:pk>", views.FollowView.as_view(), name='follow'),
    path('login/', 
         
         LoginView.as_view(template_name='users/login.html', 
            redirect_authenticated_user=True, next_page='profile'),
         
         name='login'
         ),
    path('logout/', LogoutView.as_view(next_page='post'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.AccountView.as_view(), name='profile')
]