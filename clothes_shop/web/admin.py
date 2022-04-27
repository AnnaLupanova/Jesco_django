from django.contrib import admin

from .models import Products, Type, Size, Brands, Categories

admin.site.register(Products)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Brands)
admin.site.register(Categories)