from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Comment, Recipe
from .serializers import CategorySerializer, CommentSerializer, RecipeSerializer


class BulkModelViewSet(viewsets.ModelViewSet):
    """Base ViewSet with JSON-array create, bulk update and bulk delete."""

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['patch'], url_path='bulk-update')
    def bulk_update(self, request):
        if not isinstance(request.data, list):
            return Response(
                {'error': 'Expected a list of objects.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        updated_objects = []

        for item in request.data:
            object_id = item.get('id')

            if not object_id:
                return Response(
                    {'error': 'Every object must contain id.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                instance = self.get_queryset().get(id=object_id)
            except self.queryset.model.DoesNotExist:
                return Response(
                    {'error': f'Object with id={object_id} was not found.'},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = self.get_serializer(instance, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_objects.append(serializer.data)

        return Response(updated_objects, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], url_path='bulk-delete')
    def bulk_delete(self, request):
        ids = request.query_params.get('ids')

        if not ids:
            return Response(
                {'error': 'Pass ids, for example: ?ids=1,2,3'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            ids_list = [int(pk) for pk in ids.split(',')]
        except ValueError:
            return Response(
                {'error': 'ids must be comma-separated integers.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        deleted_count, _ = self.get_queryset().filter(id__in=ids_list).delete()
        return Response({'deleted': deleted_count}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        ids = request.query_params.get('ids')

        if ids:
            return self.bulk_delete(request)

        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(BulkModelViewSet):
    """ViewSet for recipe categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class RecipeViewSet(BulkModelViewSet):
    """ViewSet for recipes."""

    queryset = Recipe.objects.select_related('category').all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        max_time = self.request.query_params.get('max_time')
        difficulty = self.request.query_params.get('difficulty')
        is_published = self.request.query_params.get('is_published')
        title = self.request.query_params.get('title')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if max_time:
            queryset = queryset.filter(cooking_time__lte=max_time)

        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        if is_published:
            queryset = queryset.filter(is_published=is_published.lower() == 'true')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class CommentViewSet(BulkModelViewSet):
    """ViewSet for recipe comments."""

    queryset = Comment.objects.select_related('recipe', 'recipe__category').all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_id = self.request.query_params.get('recipe_id')
        author_name = self.request.query_params.get('author_name')
        rating = self.request.query_params.get('rating')

        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)

        if author_name:
            queryset = queryset.filter(author_name__icontains=author_name)

        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset
