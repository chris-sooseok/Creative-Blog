from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField

User = get_user_model()

# This model has multiple fields for user setting
class Setting(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    # profile
    profile_pic = ResizedImageField(upload_to='profile_pic/', size=[128,128], quality=90, blank=True, null=True)

    def __str__(self):
        return str(self.user)

  

        


