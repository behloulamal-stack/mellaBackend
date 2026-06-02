from django.contrib import admin

from .models import CartItem ,CartModel
# Register your models here.
admin.site.register(CartModel)
admin.site.register(CartItem)

