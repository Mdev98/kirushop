from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username

    @property
    def add_to_cart(self):
        pass
