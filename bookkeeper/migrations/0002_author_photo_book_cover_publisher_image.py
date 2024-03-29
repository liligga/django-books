# Generated by Django 4.1.7 on 2023-03-21 08:38

import bookkeeper.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=bookkeeper.models.author_upload_to),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=bookkeeper.models.cover_upload_to),
        ),
        migrations.AddField(
            model_name='publisher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bookkeeper.models.publisher_upload_to),
        ),
    ]
