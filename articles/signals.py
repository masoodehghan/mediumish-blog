from django.db.models.signals import  post_delete
from .models import Post
import os

def delete_image_post(sender, instance, **kwargs):
    img_path = instance.image.path
    try:
        os.remove(img_path)
        print('done')
    except OSError:
        pass
    
post_delete.connect(delete_image_post, sender=Post)