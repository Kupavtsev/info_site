from django.contrib import admin
# from .models import Article, Tag
from . import models


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'readers_counter', 'is_approved', 'published', 'changed', 'kind', 'get_tags', 'author', 'index_page')
    list_display_links = ('title', 'kind', 'author', 'index_page')
    # search_fields = ('kind', 'published')

    def get_tags(self, obj):
        res = [s.name for s in obj.tags.all()]
        new_str = ''
        for i in res:
            # print(i[0])
            new_str += ', ' + str(i[0])
        return new_str[1:]
        # return "\n".join(str([s.name for s in obj.tags.all()]))

    # def get_topics(self, obj):
    #     res = [s.name for s in obj.topics.all()]
    #     new_str = ''
    #     for i in res:
    #         print(i[0])
    #         new_str += ', ' + str(i[0])
    #     return new_str[1:]


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('name',)


class ManufactorAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'get_distributors', 'webclick_counter', 'products', )

    def get_distributors(self, obj):
        return [s.name for s in obj.distributors.all()]

class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_manufactors', 'webclick_counter', 'products', 'services')

    def get_manufactors(self, obj):
        return [s.brand_name for s in obj.manufactories.all()]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag, TagAdmin)
# admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Manufactor, ManufactorAdmin)
admin.site.register(models.Distributor, DistributorAdmin)