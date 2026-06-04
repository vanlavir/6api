from django.contrib import admin

from .models import Category, Comment, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'cooking_time', 'difficulty', 'servings', 'is_published', 'created_at')
    search_fields = ('title', 'ingredients', 'description')
    list_filter = ('category', 'difficulty', 'is_published', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'author_name', 'rating', 'created_at')
    search_fields = ('author_name', 'text', 'recipe__title')
    list_filter = ('rating', 'created_at')
