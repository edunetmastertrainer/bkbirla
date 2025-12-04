from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.email