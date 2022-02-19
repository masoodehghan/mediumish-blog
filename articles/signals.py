from django.db.models.signals import  post_delete, post_save
from .models import Post
import os
from django.core import mail


def delete_image_post(sender, instance, **kwargs):
    img_path = instance.image.path
    try:
        os.remove(img_path)
        print('done')
    except OSError:
        pass

    
def email_post_to_followers(sender, instance, **kwargs):
    profile = instance.owner
    
    subject = f"{profile.username} has posted a new post"
    message_ = instance.body
    
    follower_emails  = []
    for profile_ in profile.followers.all():
        follower_emails.append(profile_.email)
        
        
    mail.send_mail(
        subject,
        message_,
        "masood@gmail.com",
        follower_emails
        
    )
    


post_delete.connect(delete_image_post, sender=Post)
post_save.connect(email_post_to_followers, sender=Post)