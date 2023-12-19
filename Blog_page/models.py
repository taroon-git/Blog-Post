from django.db import models
from django.contrib.auth.models import AbstractUser, Group , Permission
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Your custom fields and methods here

    # Add related_name to groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name= ('groups'),
        blank=True,
        related_name='customuser_set',  # Add this line
        related_query_name='customuser',
    )

    # Add related_name to user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name= ('user permissions'),
        blank=True,
        related_name='customuser_set',  # Add this line
        related_query_name='customuser',
    )

class Post(models.Model):
    title = models.CharField(max_length=200)
    # body = RichTextField(blank=True, null=True)
    discription = models.CharField(max_length=200,default=None)
    image = models.ImageField(upload_to='images/')


