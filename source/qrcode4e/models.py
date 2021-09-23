from django.db import models

import os
import uuid

def user_img_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("qrcode", filename)

class UserImg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=user_img_path, null=True, blank=True)
    decode_text = models.CharField(max_length=250, null=True, blank=False)
    sys_created_date = models.DateTimeField(auto_now_add=True,null=True)
    sys_updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return self.image.url
        except AttributeError: 
            return "no image"
    
    