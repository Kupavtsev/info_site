from django.shortcuts import render
from rest_framework import status, generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from .api.serializers import ArticleSerializer
from .models import Article, Manufactor, Distributor

from django.core.paginator import Paginator

# Create your views here.
# class ApiArticle(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ApiArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

ARTICLES = Article.objects.filter(kind='a')

# Great LUGS with this function
# def index_paginator(request):
#     articles = Article.objects.all()
#     paginator = Paginator(articles, 3)
#     page_num = 1
#     page = paginator.get_page(page_num)
#     context = {'articles': page.object_list}
#     return render(request, 'content/index.html', context)


class Index(ListView):
    model = Article
    template_name = "content/index.html"

    def get_context_data(self, *args, **kwargs: any):
        context = super().get_context_data(*args, **kwargs)
        # context['articles'] = ARTICLES
        context['articles'] = Article.objects.filter(index_page=True, kind="a")
        context['tech_articles'] = Article.objects.filter(index_page=True, kind="t")
        return context


class ArtclesCommonListView(ListView):
    template_name = 'content/articles_common.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(kind='a')

class ArtclesTechListView(ListView):
    template_name = 'content/articles_tech.html'
    context_object_name = 'tech_articles'

    def get_queryset(self):
        return Article.objects.filter(kind='t')

class ArticleDetailView(DetailView):
    model = Article
    # slug_url_kwarg = 'slug'
    slug_field = 'slug'



class ManufactorsListView(ListView):
    model = Manufactor
    template_name = 'content/manufactors.html'
    context_object_name = 'manufactors'

    

class DistributorsListView(ListView):
    model = Distributor
    template_name = 'content/distributors.html'
    context_object_name = 'distributors'

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))