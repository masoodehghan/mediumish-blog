import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    username = models.CharField(max_length=200, unique=True)
    name =  models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    profile_image = models.ImageField (default='profiles/default.jpg', blank=True, upload_to='profiles/')
    created = models.DateTimeField(auto_now_add=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followers')
    bio = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.username
    
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.id})
    
    




