from django.contrib.auth.models import User
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('avatars', str(instance.id), filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='library/static/avatars/', blank=True, null=True)
    nick = models.CharField(max_length=32)
    fav_system = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/profile/{}".format(self.user.profile.id)
