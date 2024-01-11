from content.models import Article, Tag, Manufactor, Distributor
from .serializers import ArticleSerializer, TagSerializer, ManufactorSerializer, DistributorSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

class ManufactorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Manufactor.objects.all()
        serializer = ManufactorSerializer(queryset, many=True)
        return Response(serializer.data)

class DistributorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Distributor.objects.all()
        serializer = DistributorSerializer(queryset, many=True)
        return Response(serializer.data)