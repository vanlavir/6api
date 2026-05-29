from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet, RecipeViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('recipes', RecipeViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
