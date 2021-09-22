from django.contrib import admin
from django.db import models
from . models import Book, Post,Book
from django.contrib import admin
# Register your models here.

admin.site.register(Post)
# admin.site.register(Book)
@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',),}
