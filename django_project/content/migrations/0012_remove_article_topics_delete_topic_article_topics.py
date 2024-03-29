# Generated by Django 4.1.3 on 2023-09-15 20:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_topic_article_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='topics',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, db_index=True, default=list, null=True, size=None, verbose_name='Tags List'),
        ),
    ]
