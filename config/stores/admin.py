from django.contrib import admin

# Register your models here.
from .models import Store, Occasion

admin.site.register(Store)
admin.site.register(Occasion)