from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email', max_length=223, blank=True, null=True)
    #photo = models.ImageField(upload_to='prof_pic', blank=True,null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(null=True, max_length=300, blank=True)

    REQUIRED_FIELDS = ['phone','email']
