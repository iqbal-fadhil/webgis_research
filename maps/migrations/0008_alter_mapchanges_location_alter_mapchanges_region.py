# Generated by Django 5.1.2 on 2024-11-25 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_mapchanges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapchanges',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.location'),
        ),
        migrations.AlterField(
            model_name='mapchanges',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.region'),
        ),
    ]
