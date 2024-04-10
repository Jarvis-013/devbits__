from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = UserManager()



class Teacher(AbstractUser):
    """
    Custom model for teachers.
    """
    
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='teacher_set',
        related_query_name='teacher',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='teacher_set',
        related_query_name='teacher',
    )

    # Set up any additional properties or methods as needed
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

   
    