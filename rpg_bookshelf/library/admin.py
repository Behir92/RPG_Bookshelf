from django.contrib import admin
from .models import (
    Author,
    Book,
    Publisher,
    System
)
# Register your models here.

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display =['name', 'edition']
    field = "__all__"

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display =['name']
    field = "__all__"

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =['name']
    field = "__all__"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =['title', 'type']
    field = "__all__"