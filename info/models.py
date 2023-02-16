from django.db import models
from datetime import datetime

# Create your models here.
class Userinfo(models.Model):
    user = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=200, null=True)

class Library(models.Model):
    book_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.name.upper() + "  $" +str(self.price)