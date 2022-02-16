from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post"),
    path('create-post', views.PostCreateView.as_view(), name='create-post'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    
]
