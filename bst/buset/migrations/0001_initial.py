# Generated by Django 3.2.8 on 2022-06-01 01:52

import buset.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30)),
                ('shop_pp', models.ImageField(upload_to='static')),
                ('shop_created', models.DateTimeField(auto_now_add=True)),
                ('shop_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_password', models.CharField(default=buset.models._create_hash, max_length=16, unique=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_pp', models.ImageField(upload_to='static')),
                ('user_role', models.CharField(max_length=6)),
                ('user_created', models.DateTimeField(auto_now_add=True)),
                ('user_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=30)),
                ('post_description', models.CharField(max_length=100)),
                ('post_price', models.DecimalField(decimal_places=0, max_digits=9)),
                ('post_text', models.TextField(blank=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='static/post_img/')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buset.posting')),
            ],
        ),
    ]
