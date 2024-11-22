from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    bio =models.TextField(null=True, blank=True)
    phone_num = models.CharField(max_length=20)
    linkedin_url = models.URLField(null=True, blank=True)

