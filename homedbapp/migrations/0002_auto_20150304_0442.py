# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homedbapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='askingprice',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='backyard',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='foundation',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='frontyard',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default=b'prop_images/house-logo-hi.png', null=True, upload_to=b'prop_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='kitchen',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='lotsize',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofbdrms',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofbthrms',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofmaster',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='offeredpricce',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='roof',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='soldprice',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='sqfootage',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='termite',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
