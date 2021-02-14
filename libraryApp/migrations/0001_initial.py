# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-10 18:17
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_no', models.CharField(blank=True, max_length=20)),
                ('book_id', models.CharField(max_length=20)),
                ('book_name', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=100)),
                ('no_of_books', models.IntegerField()),
                ('book_detail', models.TextField(default='text')),
                ('department', models.CharField(choices=[('ROM', 'Romantic'), ('REL', 'Religious'), ('FEM', 'Feminist'), ('COU', 'Courageous')], max_length=3)),
                ('rack_no', models.CharField(max_length=3)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='BORROWER',
            fields=[
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_name', models.CharField(max_length=100)),
                ('book_name', models.CharField(max_length=200)),
                ('book_id', models.CharField(max_length=20)),
                ('issue_date', models.DateField(default=datetime.date.today)),
                ('isbn_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(default=datetime.date.today)),
                ('borrower_name', models.CharField(max_length=100)),
                ('book_id', models.CharField(max_length=20)),
                ('book_name', models.CharField(max_length=200)),
                ('isbn_no', models.CharField(max_length=20)),
            ],
        ),
    ]