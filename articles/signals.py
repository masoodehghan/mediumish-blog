from django.db.models.signals import  post_delete, post_save
from .models import Post
import os
from django.core import mail


def delete_image_post(sender, instance, **kwargs):
    img_path = instance.image.path
    try:
        os.remove(img_path)
    except OSError:
        pass

    
def email_post_to_followers(sender, instance, **kwargs):
    owner_profile = instance.owner
    
    subject = f"{owner_profile.username} has posted a new post"
    message_ = f"link to the post \n http://127.0.0.1:8000/post/{instance.slug}"
    
    
    follower_emails  = []
    for profile in owner_profile.followers.all():
        follower_emails.append(profile.email)
        
        
    mail.send_mail(
        subject,
        message_,
        "masood@gmail.com",
        follower_emails,
        fail_silently=True
    )
    
    


post_delete.connect(delete_image_post, sender=Post)
post_save.connect(email_post_to_followers, sender=Post)