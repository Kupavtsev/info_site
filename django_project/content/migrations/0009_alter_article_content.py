# Generated by Django 4.1.3 on 2022-12-21 15:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_alter_article_image_alter_article_image_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
    ]
