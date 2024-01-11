from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (DateTimeRangeField, ArrayField, HStoreField,
                                            CICharField, JSONField, RangeOperators)
# from django.contrib.postgres.indexes import GistIndex, OpClass

from ckeditor.fields import RichTextField



class Tag(models.Model):
    name = ArrayField(base_field=models.CharField(max_length=50), db_index=True, default=list, null=True, blank=True, verbose_name='Tags List')

    def __ascii__(self):
        return self.name

    def __str__(self):
        res = [x for x in self.name]
        new_str = ''
        for i in res:
            # print(i)
            new_str += str(i)
        return new_str[:]
    
# class Topic(models.Model):
#     name = ArrayField(base_field=models.CharField(max_length=250), db_index=True, default=list, null=True, blank=True, verbose_name='Topics')

#     def __ascii__(self):
#         return self.name

#     def __str__(self):
#         res = [x for x in self.name]
#         new_str = ''
#         for i in res:
#             print(i)
#             new_str += str(i)
#         return new_str[:]

# class VotesAndStars(models.Model):
#     stars = None
#     votes_positive = models.SmallIntegerField(verbose_name='Votes positive')
#     votes_megative = models.SmallIntegerField(verbose_name='Votes negative')


class Article(models.Model):

    # def get_absolute_url(self):
    #     return f'/articles/{self.kind}'

    class Kinds(models.TextChoices):
                    Article = 'a', 'Article Common'
                    TechInfo = 't', 'Tech Article'
                    __empty__ = 'Choice type of article'


    title = models.CharField(max_length=250, db_index=True, verbose_name='Title')
    slug = models.SlugField(unique=True, max_length=200, verbose_name='slug')
    description = models.TextField(db_index=True, verbose_name='Description')
    # content = models.TextField(verbose_name='Content')
    content = RichTextField(null=True, blank=True, verbose_name='Content')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Image main')
    image_mobile = models.ImageField(upload_to='content/static/media/', null=True, blank=True, verbose_name='Image for mobile')
    article_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Url in Article')
    published = models.DateField(auto_now_add=True, verbose_name="Published")
    changed = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Changed")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Author')
    is_approved = models.BooleanField(default=False, verbose_name='Is approved')
    kind = models.CharField(max_length=1, choices=Kinds.choices, default=Kinds.Article)
    tags = models.ManyToManyField(Tag)
    # topics = models.ManyToManyField(Topic)
    timetoread = models.CharField(max_length=20, default='3min', null=True, blank=True, verbose_name='timetoread')
    topics = ArrayField(models.CharField(max_length=400), db_index=True, default=list, null=True, blank=True, verbose_name='topics')
    index_page = models.BooleanField(default=False, verbose_name='Main page')
    
    readers_counter = models.SmallIntegerField(default=0, verbose_name='Count')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/articles/detail/{self.slug}'
        # return reverse('article_detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=('title', 'description'),
    #                             name='i_article_title_description',
    #                             opclasses=('varchar_pattern_ops', 'bpchar_pattern_ops'))
    #     ]

    #     # if title and description is matched
    #     constraints = [
    #         ExclusionConstraint(name='c_article_title_description',
    #                             expressions=[('title', RangeOperators.EQUAL),
    #                             ('description', RangeOperators.EQUAL)])
    #         ]



class Manufactor(models.Model):
    brand_name = models.CharField(unique=True, max_length=250, db_index=True, verbose_name='Brand Name')
    image = models.ImageField(upload_to='media/manufactor', null=True, blank=True, verbose_name='Brand Image')
    # brand_label = models.ImageField(upload_to='manufactors/media', null=True, blank=True, verbose_name='Label')
    slug = models.SlugField(unique=True, max_length=200, blank=True, verbose_name='slug')
    location = models.TextField(max_length=200, null=True, blank=True, verbose_name='Location')
    profile = models.TextField(null=True, blank=True, verbose_name='Profile')
    url_company = models.URLField(max_length=200, null=True, blank=True, verbose_name='Company Url')
    tel = models.CharField(max_length=100, null=True, blank=True, verbose_name='Tel')
    email = models.EmailField(null=True, blank=True, max_length=250)
    products = ArrayField(base_field=models.CharField(max_length=50), db_index=True, default=list, null=True, blank=True, verbose_name='Products')
    services = ArrayField(base_field=models.CharField(max_length=50), db_index=True, default=list, null=True, blank=True, verbose_name='Services')
    distributors = models.ManyToManyField('Distributor', null=True, blank=True)

    webclick_counter = models.SmallIntegerField(default=0, verbose_name='Count')

    # def __ascii__(self):
    #     return self.brand_name

    def __str__(self):
        res = [x for x in self.brand_name]
        new_str = ''
        for i in res:
            # print(i)
            new_str += str(i)
        return new_str[:]

    # class Meta:
    #     constraints = [
    #         ExclusionConstraint(name='c_brand_name_url_company_description',
    #                             expressions=[('brand_name', RangeOperators.EQUAL),
    #                             ('url_company', RangeOperators.EQUAL)])]

    # def __str__(self):
    #     return self.brand_name


class Distributor(models.Model):
    name = models.CharField(unique=True, max_length=250, db_index=True, verbose_name='Name')
    image = models.ImageField(upload_to='media/distributor', null=True, blank=True, verbose_name='Brand Image')
    # brand_label = models.ImageField(upload_to='distributors/media', null=True, blank=True, verbose_name='Label')
    slug = models.SlugField(unique=True, max_length=200, blank=True, verbose_name='slug')
    location = models.TextField(max_length=200, null=True, blank=True, verbose_name='Location')
    profile = models.TextField(null=True, blank=True, verbose_name='Profile')
    url_distributor = models.URLField(max_length=200, null=True, blank=True, verbose_name='Distributor Url')
    tel = models.CharField(max_length=100, null=True, blank=True, verbose_name='Tel')
    email = models.EmailField(null=True, blank=True, max_length=250)
    products = ArrayField(base_field=models.CharField(max_length=50), db_index=True, default=list, null=True, blank=True, verbose_name='Products Dist')
    services = ArrayField(base_field=models.CharField(max_length=50), db_index=True, default=list, null=True, blank=True, verbose_name='Services Dist')
    manufactories = models.ManyToManyField(Manufactor, null=True, blank=True)
    my_contact = models.JSONField(null=True, blank=True, verbose_name='My Contact')

    webclick_counter = models.SmallIntegerField(default=0, verbose_name='Count')

    # class Meta:
    #     constraints = [
    #         ExclusionConstraint(name='c_name_url_distributor_description',
    #                             expressions=[('name', RangeOperators.EQUAL),
    #                             ('url_distributor', RangeOperators.EQUAL)])]

    # def __str__(self):
    #     return self.name