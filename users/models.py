import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.urls import reverse

class Profile(models.Model):
    username = models.CharField(max_length=200, unique=True)
    name =  models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.id})
    
    


# signals for creating profile when a user created
def create_user(sender, instance, created,  **kwargs):
    
    if created:    
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username.lower(),
            name = user.first_name,
            email = user.email
        )
        
        

def delete_user(sender, instance, **kawrgs):
    user = instance.user
    user.delete()


# def delete_profile(sender, instance, **kawrgs):
#     profile = instance.profile
#     profile.delete()


def update_user(sender, instance, created, **kwargs):    
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username.lower()
        user.email = profile.email
        user.save()
        
        
        
post_save.connect(create_user, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
# post_delete.connect(delete_profile, sender=User)
