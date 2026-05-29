from django.contrib import admin

from .models import Category, Comment, Recipe


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
