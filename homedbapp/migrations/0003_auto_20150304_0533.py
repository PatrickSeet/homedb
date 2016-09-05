# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homedbapp', '0002_auto_20150304_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='askingprice',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='backyard',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='foundation',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='frontyard',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='kitchen',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='lotsize',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofbdrms',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofbthrms',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='numofmaster',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='offeredpricce',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='propertytype',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='roof',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='soldprice',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='sqfootage',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='termite',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='xcoordinate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='ycoordinate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
