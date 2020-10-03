from django.contrib import admin
from .models import Heart, Diabetes, Feedback

# Register your models here.
admin.site.register((Heart, Diabetes, Feedback))

admin.site.site_header = "Disease Predictor Admin"
admin.site.site_title = "Disease Predictor Admin Portal"
admin.site.index_title = "Welcome to Disease Predictor Portal"
