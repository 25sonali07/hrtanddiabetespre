from django.contrib import admin
from .models import Heart, Diabetes

# Register your models here.
admin.site.register((Heart, Diabetes))
