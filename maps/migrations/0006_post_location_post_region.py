# Generated by Django 5.1.2 on 2024-11-19 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='maps.location'),
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='maps.region'),
        ),
    ]