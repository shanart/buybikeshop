from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "users/%s/%s" %(instance.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userpic     = models.ImageField(
                        upload_to=upload_location,
                        null=True,
                        blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.user.username
