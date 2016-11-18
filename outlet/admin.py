from django.contrib import admin
from .models import Category, Tag, Item, UserProfile, Order, Cart
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Cart)