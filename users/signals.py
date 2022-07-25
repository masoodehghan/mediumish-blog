from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

# signals for creating profile when a user created


def create_user(sender, instance, created, **kwargs):

    if created:
        user = instance

        Profile.objects.create(
            user=user,
            username=user.username.lower(),
            name=user.first_name,
            email=user.email
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
