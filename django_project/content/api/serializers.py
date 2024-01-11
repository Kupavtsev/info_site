from rest_framework import serializers

from content.models import Article, Tag, Manufactor, Distributor

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'description', 'content', 'kind', 'tags')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class ManufactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactor
        fields = ('id', 'brand_name', 'slug', 'profile', 'email', )


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ('id', 'name', 'slug', 'profile', 'email', )
