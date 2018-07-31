# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20160831_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '帖子表', 'verbose_name_plural': '帖子表'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '板块表', 'verbose_name_plural': '板块表'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论表', 'verbose_name_plural': '评论表'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(blank=True, height_field=150, null=True, upload_to='uploads', verbose_name='头像', width_field=150),
        ),
    ]