from rest_framework import serializers

from .models import Category, Comment, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'category',
            'category_id',
            'cooking_time',
            'difficulty',
            'servings',
            'is_published',
            'ingredients',
            'description',
            'created_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    recipe = serializers.StringRelatedField(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe',
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'recipe_id', 'author_name', 'text', 'rating', 'created_at']
