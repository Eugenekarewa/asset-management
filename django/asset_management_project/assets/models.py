# assets/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    # Add more profile fields as needed

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    state = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used')])
    serial_number = models.CharField(max_length=50, unique=True)
    # Add more fields as needed

    def __str__(self):
        return self.name

class Lease(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    leased_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lease_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Lease of {self.item.name} to {self.leased_by.username}"
