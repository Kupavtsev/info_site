# Generated by Django 4.1.3 on 2022-11-24 15:19

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, db_index=True, default=list, null=True, size=None, verbose_name='Tags List')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('description', models.TextField(db_index=True, verbose_name='Description')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/media', verbose_name='Image main')),
                ('image_mobile', models.ImageField(blank=True, null=True, upload_to='articles/media', verbose_name='Image for mobile')),
                ('article_url', models.URLField(blank=True, null=True, verbose_name='Url in Article')),
                ('published', models.DateField(auto_now_add=True, verbose_name='Published')),
                ('changed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Changed')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is approved')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', models.ManyToManyField(to='content.tag')),
            ],
        ),
    ]
