# Generated by Django 4.1.3 on 2023-09-15 20:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_remove_article_topics_delete_topic_article_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, db_index=True, default=list, null=True, size=None, verbose_name='topics'),
        ),
    ]
