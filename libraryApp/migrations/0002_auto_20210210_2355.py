# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-10 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='image',
            new_name='book_image',
        ),
    ]
