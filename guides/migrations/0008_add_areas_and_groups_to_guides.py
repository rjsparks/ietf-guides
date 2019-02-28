# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0007_populate_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='areas',
            field=models.ManyToManyField(to='guides.Area', verbose_name='What IETF area(s) are you involved in?'),
        ),
        migrations.AddField(
            model_name='guide',
            name='groups',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Which working groups are you willing to guide for?'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='groups',
            field=models.CharField(help_text='see <a href="https://www.ietf.org/how/wgs">https://wwww.ietf.org/how/wgs</a>', max_length=256, verbose_name='Which working groups are you most interested in?'),
        ),
    ]
