# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medios_libres', '0002_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='WpCommentmeta',
            fields=[
                ('meta_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_id', models.BigIntegerField()),
                ('meta_key', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wp_commentmeta',
            },
        ),
        migrations.CreateModel(
            name='WpComments',
            fields=[
                ('comment_id', models.BigAutoField(db_column=b'comment_ID', primary_key=True, serialize=False)),
                ('comment_post_id', models.BigIntegerField(db_column=b'comment_post_ID')),
                ('comment_author', models.TextField()),
                ('comment_author_email', models.CharField(max_length=100)),
                ('comment_author_url', models.CharField(max_length=200)),
                ('comment_author_ip', models.CharField(db_column=b'comment_author_IP', max_length=100)),
                ('comment_date', models.DateTimeField()),
                ('comment_date_gmt', models.DateTimeField()),
                ('comment_content', models.TextField()),
                ('comment_karma', models.IntegerField()),
                ('comment_approved', models.CharField(max_length=20)),
                ('comment_agent', models.CharField(max_length=255)),
                ('comment_type', models.CharField(max_length=20)),
                ('comment_parent', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_comments',
            },
        ),
        migrations.CreateModel(
            name='WpLinks',
            fields=[
                ('link_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('link_url', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
                ('link_image', models.CharField(max_length=255)),
                ('link_target', models.CharField(max_length=25)),
                ('link_description', models.CharField(max_length=255)),
                ('link_visible', models.CharField(max_length=20)),
                ('link_owner', models.BigIntegerField()),
                ('link_rating', models.IntegerField()),
                ('link_updated', models.DateTimeField()),
                ('link_rel', models.CharField(max_length=255)),
                ('link_notes', models.TextField()),
                ('link_rss', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'wp_links',
            },
        ),
        migrations.CreateModel(
            name='WpPostmeta',
            fields=[
                ('meta_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_id', models.BigIntegerField()),
                ('meta_key', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wp_postmeta',
            },
        ),
        migrations.CreateModel(
            name='WpPosts',
            fields=[
                ('id', models.BigAutoField(db_column=b'ID', primary_key=True, serialize=False)),
                ('post_author', models.BigIntegerField()),
                ('post_date', models.DateTimeField()),
                ('post_date_gmt', models.DateTimeField()),
                ('post_content', models.TextField()),
                ('post_title', models.TextField()),
                ('post_excerpt', models.TextField()),
                ('post_status', models.CharField(max_length=20)),
                ('comment_status', models.CharField(max_length=20)),
                ('ping_status', models.CharField(max_length=20)),
                ('post_password', models.CharField(max_length=255)),
                ('post_name', models.CharField(max_length=200)),
                ('to_ping', models.TextField()),
                ('pinged', models.TextField()),
                ('post_modified', models.DateTimeField()),
                ('post_modified_gmt', models.DateTimeField()),
                ('post_content_filtered', models.TextField()),
                ('post_parent', models.BigIntegerField()),
                ('guid', models.CharField(max_length=255)),
                ('menu_order', models.IntegerField()),
                ('post_type', models.CharField(max_length=20)),
                ('post_mime_type', models.CharField(max_length=100)),
                ('comment_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_posts',
            },
        ),
        migrations.CreateModel(
            name='WpTermmeta',
            fields=[
                ('meta_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('term_id', models.BigIntegerField()),
                ('meta_key', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wp_termmeta',
            },
        ),
        migrations.CreateModel(
            name='WpTermRelationships',
            fields=[
                ('object_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('term_taxonomy_id', models.BigIntegerField()),
                ('term_order', models.IntegerField()),
            ],
            options={
                'db_table': 'wp_term_relationships',
            },
        ),
        migrations.CreateModel(
            name='WpTerms',
            fields=[
                ('term_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('term_group', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_terms',
            },
        ),
        migrations.CreateModel(
            name='WpTermTaxonomy',
            fields=[
                ('term_taxonomy_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('term_id', models.BigIntegerField()),
                ('taxonomy', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('parent', models.BigIntegerField()),
                ('count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_term_taxonomy',
            },
        ),
    ]
