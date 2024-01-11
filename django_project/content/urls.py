from django.urls import path

from . import views

app_name = 'content'


urlpatterns = [
   path('distributors/', views.DistributorsListView.as_view(), name='distributors'),
   path('manufactors/', views.ManufactorsListView.as_view(), name='manufactors'),
   path('articles/tech/', views.ArtclesTechListView.as_view(), name='articles_tech'),
   path('articles/common/', views.ArtclesCommonListView.as_view(), name='articles_common'),
   path('articles/detail/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
   path('<str:page>/', views.other_page, name='other_page'),
   # path('articles/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
   path('', views.Index.as_view(), name='index'),
   # path('', views.index_paginator, name='index'),
]