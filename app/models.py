from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class newUser(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    user_permissions = models.ManyToManyField( # Solved the user field relationship conflict
        'auth.permission',
        related_name='newuser_user_permissions',
        blank=True
    )

    groups = models.ManyToManyField( # Solved the group field relationship conflict
        'auth.Group',
        related_name='newuser_groups',
        blank=True
    )


    def __str__(self):
        return self.username