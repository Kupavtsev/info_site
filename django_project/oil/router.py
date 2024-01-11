from content.api.viewsets import ArticleViewSet, TagViewSet, ManufactorViewSet, DistributorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('tags', TagViewSet, basename='tag')
router.register('manufactors', ManufactorViewSet, basename='manufactor')
router.register('distributors', DistributorViewSet, basename='distributor')
