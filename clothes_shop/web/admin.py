from django.contrib import admin
from .models import Products, Type, Size, Brands, Categories


@admin.register(Products)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('id','title','price')


@admin.register(Type)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Size)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Brands)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Categories)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('id','name')
