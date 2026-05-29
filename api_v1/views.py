from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Comment, Recipe
from .serializers import CategorySerializer, CommentSerializer, RecipeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()

        category = self.request.query_params.get('category')
        max_time = self.request.query_params.get('max_time')
        difficulty = self.request.query_params.get('difficulty')
        is_published = self.request.query_params.get('is_published')

        if category:
            queryset = queryset.filter(category_id=category)
        if max_time:
            queryset = queryset.filter(cooking_time__lte=max_time)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        if is_published:
            queryset = queryset.filter(is_published=is_published.lower() == 'true')

        return queryset

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'])
    def bulk_update(self, request):
        updated_recipes = []

        for item in request.data:
            recipe_id = item.get('id')
            try:
                recipe = Recipe.objects.get(id=recipe_id)
            except Recipe.DoesNotExist:
                continue

            serializer = self.get_serializer(recipe, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_recipes.append(serializer.data)

        return Response(updated_recipes)

    @action(detail=False, methods=['delete'])
    def bulk_delete(self, request):
        ids = request.data.get('ids', [])
        deleted_count, _ = Recipe.objects.filter(id__in=ids).delete()
        return Response({'deleted': deleted_count})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        recipe_id = self.request.query_params.get('recipe_id')
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)
        return queryset
