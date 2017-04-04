from django.contrib.auth.models import User
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('avatars', str(instance.id), filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    nick = models.CharField(max_length=32)
    fav_system = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"