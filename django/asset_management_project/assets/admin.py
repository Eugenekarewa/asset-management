# assets/admin.py
from django.contrib import admin
from .models import Item, Lease

admin.site.register(Item)
admin.site.register(Lease)
