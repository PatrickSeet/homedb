from django.contrib import admin
from homedbapp.models import Shopper
from homedbapp.models import Property
from homedbapp.models import PropertyNotes

# Register your models here.
admin.site.register(Shopper)
admin.site.register(Property)
admin.site.register(PropertyNotes)